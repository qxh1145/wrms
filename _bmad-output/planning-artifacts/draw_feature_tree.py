# Feature tree for Report 1 §6.1, styled after the COS template (Visual Paradigm mind map look).
# Run: python3 draw_feature_tree.py  -> report1-section6-feature-tree.png
from PIL import Image, ImageDraw, ImageFont

ROOT = "Citizen Field\nReport Intake and\nTask Assignment\nSystem (WRMS)"
TREE = [  # (L1 label, [L2...]); first 5 go right, rest left
    ("Citizen\nReporting", ["Submit Report", "Location Pinning", "Data Consent", "Status Tracking"]),
    ("AI\nAnalysis", ["Photo Screening", "Duplicate Grouping", "Priority Suggestion", "Keyword Rules"]),
    ("Report\nIntake", ["Review Queue", "Accept or Reject", "Final Priority", "Jurisdiction Closure"]),
    ("Task\nRouting", ["Routing Rules", "Unit Suggestion", "Parallel Tasks", "Police Coordination"]),
    ("Task\nTracking", ["Task Assignment", "Deadline Setting", "Progress Tracking", "Overdue Reminders"]),
    ("Field\nExecution", ["Accept or Decline", "Photo Evidence", "Result Acceptance"]),
    ("Hazard\nSafety", ["Hazard Flag", "Red Alert", "Assignment Lock"]),
    ("Monitoring", ["Hotspot Map", "Statistics Dashboard", "Leadership View"]),
    ("Administration", ["Staff Accounts", "Category Catalog", "Unit Management", "System Configuration"]),
]
RIGHT, LEFT = TREE[:5], TREE[5:]

S = 2
ROW, GAP, MARGIN = 40 * S, 28 * S, 40 * S
ROOT_GAP, L2_GAP, UL_PAD = 120 * S, 70 * S, 14 * S
ROOT_FILL, L1_FILL = (68, 94, 190), (233, 234, 240)
LINE, TEXT, GREEN = (110, 110, 110), (60, 60, 60), (110, 180, 80)


def font(size):
    for p in ["/System/Library/Fonts/Supplemental/Tahoma.ttf", "/System/Library/Fonts/Supplemental/Verdana.ttf",
              "/System/Library/Fonts/Supplemental/Arial.ttf", "DejaVuSans.ttf"]:
        try:
            return ImageFont.truetype(p, size)
        except OSError:
            continue
    return ImageFont.load_default()


F_ROOT, F_L1, F_L2 = font(24 * S), font(20 * S), font(15 * S)
_m = ImageDraw.Draw(Image.new("RGB", (1, 1)))


def tsize(text, f):
    b = _m.multiline_textbbox((0, 0), text, font=f, spacing=4 * S, align="center")
    return b[2] - b[0], b[3] - b[1]


rw, rh = tsize(ROOT, F_ROOT)
RW, RH = rw + 50 * S, rh + 50 * S
L1W = max(tsize(n, F_L1)[0] for n, _ in TREE) + 40 * S
L1H = max(tsize(n, F_L1)[1] for n, _ in TREE) + 28 * S
KIDW = max(tsize(k, F_L2)[0] for _, ks in TREE for k in ks) + UL_PAD
HALF = RW // 2 + ROOT_GAP + L1W + L2_GAP + KIDW
W = 2 * (HALF + MARGIN)


def side_h(side):
    return sum(len(k) * ROW for _, k in side) + GAP * (len(side) - 1)


H = max(side_h(RIGHT), side_h(LEFT), RH) + 2 * MARGIN
CX, CY = W // 2, H // 2
W, H, CX, CY = int(W), int(H), int(W) // 2, int(H) // 2
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)


def curve(p0, p3):
    (x0, y0), (x3, y3) = p0, p3
    dx = (x3 - x0) * 0.5
    pts = []
    for i in range(41):
        t = i / 40
        a, b, c, e = (1 - t) ** 3, 3 * (1 - t) ** 2 * t, 3 * (1 - t) * t ** 2, t ** 3
        pts.append((a * x0 + b * (x0 + dx) + c * (x3 - dx) + e * x3, a * y0 + b * y0 + c * y3 + e * y3))
    d.line(pts, fill=LINE, width=2 * S, joint="curve")


def draw_side(side, s):  # s = +1 right, -1 left
    y = (H - side_h(side)) // 2
    rx = CX + s * RW // 2
    inner = rx + s * ROOT_GAP
    outer = inner + s * L1W
    for label, kids in side:
        mid = y + len(kids) * ROW // 2
        sy = min(max(mid, CY - RH // 2 + 16 * S), CY + RH // 2 - 16 * S)
        curve((rx, sy), (inner, mid))
        x0, x1 = sorted([inner, outer])
        d.rounded_rectangle([x0, mid - L1H // 2, x1, mid + L1H // 2], 8 * S, fill=L1_FILL)
        d.multiline_text(((x0 + x1) // 2, mid), label, font=F_L1, fill=TEXT, anchor="mm", align="center", spacing=4 * S)
        r, cx = 8 * S, outer + s * 12 * S
        for i, kid in enumerate(kids):
            uy = y + i * ROW + int(ROW * 0.8)
            u0 = outer + s * L2_GAP
            u1 = u0 + s * (tsize(kid, F_L2)[0] + UL_PAD)
            curve((cx + s * r, mid), (u0, uy))
            d.line([u0, uy, u1, uy], fill=LINE, width=2 * S)
            d.text((min(u0, u1) + UL_PAD // 2, uy - 4 * S), kid, font=F_L2, fill=TEXT, anchor="ld")
            assert MARGIN // 2 <= min(u0, u1) and max(u0, u1) <= W - MARGIN // 2, kid
        d.ellipse([cx - r, mid - r, cx + r, mid + r], fill=(235, 248, 230), outline=GREEN, width=2 * S)
        d.line([cx - r // 2, mid, cx + r // 2, mid], fill=GREEN, width=2 * S)
        y += len(kids) * ROW + GAP


draw_side(RIGHT, 1)
draw_side(LEFT, -1)
d.rounded_rectangle([CX - RW // 2, CY - RH // 2, CX + RW // 2, CY + RH // 2], 6 * S, fill=ROOT_FILL)
d.multiline_text((CX, CY), ROOT, font=F_ROOT, fill="white", anchor="mm", align="center", spacing=4 * S)

img.save("report1-section6-feature-tree.png", dpi=(300, 300))
print("ok", img.size)
