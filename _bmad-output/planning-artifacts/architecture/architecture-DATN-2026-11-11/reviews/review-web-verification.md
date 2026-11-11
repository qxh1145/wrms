# Review: web verification of ARCHITECTURE-SPINE (2026-11-11)

Method: npm registry, PyPI, nodejs.org dist index, GitHub releases API, official docs (docs.nestjs.com, zod.dev, docs.expo.dev, docs.zaloplatforms.com, unpkg type files for drizzle-orm@0.45.4). Reviewer did not run any code.

## Verdict
Stack table is almost entirely accurate, with one real error (@node-rs/argon2) and a few unchecked or imprecise fit claims; none threaten the architecture.

## Stack rows

CONFIRMED: Node 26 LTS (v26.13.0, codename Lithium; nodejs.org/dist/index.json); pnpm 12.18.0; TypeScript 6.0.3 exists (but `latest` is 7.0.2); zod 4.6.7; NestJS 12.4.2; @nestjs/schedule 12.0.3 (peer Nest 11||12); @nestjs/throttler 6.7.1 (peer includes 12); drizzle-orm 0.45.4 (`latest` tag; 1.0.0-rc.5 exists under `rc`); drizzle-kit 0.31.11; PostgreSQL 18.6; sharp 0.35.5; firebase-admin 14.5.0; @turf/boolean-point-in-polygon 7.4.0; React 19.3.1; Vite 8.3.8; React Router 8.5.1 (peer react >=19.2.7); TanStack Query 5.107.1; Ant Design 6.7.0 (peer react >=18); maplibre-gl 6.17.0; zmp-cli 4.0.7; zmp-sdk 2.53.4; zmp-ui 1.11.15-2; zmp-vite-plugin 1.1.6 (peer vite ^4.2 || ^5); expo 58.0.23; expo-notifications 58.1.8; @maplibre/maplibre-react-native 11.5.1; eas-cli 27.7.2; FastAPI 0.162.4; Pydantic 2.14.3 (spine says "2.14"; fine); Uvicorn 0.54.0; PyTorch 2.15.0 (has cp314 wheels); ONNX Runtime 1.31.1; Caddy 2.11.9; Docker Compose 5.7.0.

WRONG:
- **@node-rs/argon2: spine "0.35 (0.35.5)"; real latest is 2.2.2** (https://registry.npmjs.org/@node-rs/argon2/latest). 0.35.5 is the sharp version; no 0.35 line of argon2 exists in recent releases (versions list ends 2.0.2 ... 2.2.2). Pinning "0.35" would fail install.

COULD NOT CONFIRM (not independently): React Native 0.88 and React 19.3.0 inside Expo 58 (expo package peers are `*`; relies on memlog); Python 3.14 as the right pick (exists; 3.15.2 claim from memlog not checked); EAS "15 free Android builds" figure; Expo SDK 58 release date 15/10/2026.

## Fit claims (2a-2h)

| Item | Result |
| --- | --- |
| 2a Drizzle `.for('update')` | CONFIRMED in types: `for(strength, config?)` on pg select (unpkg drizzle-orm@0.45.4 pg-core/query-builders/select.d.ts). Docs page I fetched did not mention it; the types do. |
| 2a partial unique index | CONFIRMED in types: `IndexBuilder.where(sql)` and `unique` flag exist. NOT confirmed: that drizzle-kit 0.31 emits correct SQL for partial unique indexes and for a `where` using an enum/boolean column. Spike R1 already plans to test it; good. |
| 2a trigger blocking UPDATE/DELETE | drizzle-kit does not model triggers; needs a hand-written custom migration (`drizzle-kit generate --custom`). Spine does not say so. |
| 2b NestJS 12 + TS 6 + Node 26 | CONFIRMED: docs.nestjs.com/migration-guide says schematics v12 needs TypeScript 6 as peer (npm shows `>=6.0.0`, so TS 7 also allowed), CLI needs Node v22.22.3+/24.15+/26+, app runs on 20.19+/22.12+; core is ESM, CJS apps work via require(esm); Jest needs Node 24.9+. Spine wording "NestJS 12 yêu cầu dòng 6" is slightly off: it is `>=6`. |
| 2b @nestjs/schedule | CONFIRMED peer range. NestJS + Drizzle without official package: no official Nest-Drizzle module exists; custom provider is the normal pattern (not source-verified, low risk). |
| 2c zod 4 strips unknown keys | CONFIRMED (zod.dev/api: `z.object` strips; `strictObject`/`looseObject` exist). |
| 2d Expo | CONFIRMED: `getDevicePushTokenAsync` returns native FCM token; remote push on Android needs dev build since SDK 53 (docs.expo.dev notifications page, SDK 58); `android.buildType: "apk"` in eas.json (docs.expo.dev/build-reference/apk). `firebase-admin` HTTP v1: standard, not re-fetched. |
| 2e maplibre-react-native 11 | CONFIRMED peers: expo >=54, react >=19.1, react-native >=0.80. Expo 58 satisfies. No Google key: memlog states, not re-verified. MapLibre GL JS raster source + heatmap layer: CONFIRMED (docs list RasterTileSource and heatmap examples). |
| 2f Zalo | `getAccessToken`, `getPhoneNumber`, `getLocation`, `nativeStorage` pages exist (docs.zaloplatforms.com/docs/MA/api/...). `/v2.0/me/info` with headers `access_token`, `code`, `secret_key`, token one-use and 2 minutes: CONFIRMED on the getPhoneNumber page. `GET graph.zalo.me/v2.0/me` returning app-scoped `id`: NOT on the getAccessToken page I fetched (it only says the token alone exposes the user id from SDK 2.35.0); the memlog cites it, but I could not find it on the MA docs. zmp-ui React 19 support: no peer range declared on npm; unknown, spine already pins React 18.2. |
| 2g | Ordinary features. Caveat: session-level `pg_advisory_lock` on a pooled connection can unlock on the wrong connection; use `pg_try_advisory_xact_lock` inside a transaction. Spine does not say which. |
| 2h Caddy | Static SPA + `/api` reverse proxy + automatic HTTPS is standard (docs automatic-https page exists). |

## Findings, ranked

1. **HIGH** - Stack row `@node-rs/argon2 0.35 (0.35.5)`. Real latest 2.2.2; 0.35.5 is sharp's number. Memlog claims it was verified, so the check was not reliable. Fix: change to `2 (2.2.2)` and recheck other memlog "verified" numbers that happen to coincide.
2. **MEDIUM** - AD-6 `GET /v2.0/me` returning `id` is load-bearing for all identity and is not confirmed on the MA docs I could reach; memlog also says appsecret_proof is undocumented (S4). Fix: make the spike S3/S4 a hard gate before sprint 1 and cite the exact doc URL for `/v2.0/me` in the memlog.
3. **MEDIUM** - AD-9 trigger blocking UPDATE/DELETE and any other trigger are not generated by drizzle-kit. Fix: state in AD-9 that these ship as hand-written custom migrations and add the trigger to the R1 first-sprint test.
4. **MEDIUM** - AD-13 advisory lock: not stated that it must be transaction-scoped (`pg_try_advisory_xact_lock`) given a connection pool. Fix: say so in AD-13.
5. **MEDIUM** - Drizzle partial unique index migration output via drizzle-kit 0.31 unverified (types support `.where`). R1 already schedules a test; fix: make that test an exit criterion of sprint 1, including AD-8's "Declined chưa xét" predicate.
6. **LOW** - TypeScript row: `latest` is 7.0.2; spine pins 6.0.3 and says Nest 12 "requires" line 6 (peer is `>=6.0.0`). Fix: reword to "pinned to 6 for tooling compatibility", and note TS 7 exists.
7. **LOW** - Drizzle: 1.0.0-rc.5 exists on npm. Pinning 0.45 is fine; note the decision to stay on 0.x.
8. **LOW** - Unconfirmed in memlog or by me: RN 0.88 / React 19.3.0 in Expo 58, EAS free build count, "no Google key" for maplibre-rn, Python 3.15.2. None changes a decision; label as memlog-sourced.
9. **LOW** - zmp-ui has no declared React peer and requires `react-router-dom` ^6||^7 (its dependency); Mini App therefore carries a different router from web (React Router 8). Spine already isolates the Mini App; add the router note to Stack row.
10. **LOW** - Starter defaults: spine uses no scaffolder for NestJS/Vite/Expo/zmp-cli outputs; the note "code is the source of truth once it exists" covers this, but zmp-cli's template defaults (React 18.2, Vite 5) were taken from memlog only.
