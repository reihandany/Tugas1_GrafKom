import plotly.graph_objects as go
import numpy as np

# Fungsi transformasi
def translate(points, dx=0, dy=0, dz=0):
    return [[x + dx, y + dy, z + dz] for x, y, z in points]

def scale(points, sx=1, sy=1, sz=1):
    return [[x * sx, y * sy, z * sz] for x, y, z in points]

def rotate_z(points, angle_deg):
    angle = np.radians(angle_deg)
    cos_a, sin_a = np.cos(angle), np.sin(angle)
    return [[x * cos_a - y * sin_a, x * sin_a + y * cos_a, z] for x, y, z in points]

# Persegi (dinding kiri)
square = [
    [0, 0, 0],
    [0, 0, 2],
    [0, 2, 2],
    [0, 2, 0]
]
square = scale(square, sx=1, sy=1, sz=1.2)
square = translate(square, dx=0, dy=0, dz=0)

# Persegi panjang (dinding kanan)
rectangle = [
    [4, 0, 0],
    [4, 0, 2],
    [4, 2, 2],
    [4, 2, 0]
]
rectangle = scale(rectangle, sx=1, sy=1.1, sz=1)
rectangle = translate(rectangle, dx=0.2, dy=0, dz=0)

# Atap segitiga depan
triangle_front = [
    [0, 0, 2],
    [4, 0, 2],
    [2, 0, 3.5]
]
triangle_front = rotate_z(triangle_front, angle_deg=0)
triangle_front = translate(triangle_front, dx=0, dy=0, dz=0)

# Atap segitiga belakang
triangle_back = [
    [0, 2, 2],
    [4, 2, 2],
    [2, 2, 3.5]
]
triangle_back = rotate_z(triangle_back, angle_deg=0)
triangle_back = translate(triangle_back, dx=0, dy=0, dz=0)

# Dinding depan dan belakang
front = [
    [0, 0, 0], [4, 0, 0],
    [4, 0, 2], [0, 0, 2]
]
back = [
    [0, 2, 0], [4, 2, 0],
    [4, 2, 2], [0, 2, 2]
]

# Atap miring kiri & kanan
roof_left = [triangle_front[0], triangle_back[0], triangle_back[2], triangle_front[2]]
roof_right = [triangle_front[1], triangle_back[1], triangle_back[2], triangle_front[2]]

# Lantai bawah
bottom = [
    [0, 0, 0], [4, 0, 0], [4, 2, 0], [0, 2, 0]
]

# Gabungkan semua titik
all_faces = [
    (square, 'lightskyblue'),
    (rectangle, 'navy'),
    (front, 'lightskyblue'),
    (back, 'lightskyblue'),
    (triangle_front, 'gold'),
    (triangle_back, 'gold'),
    (roof_left, 'gold'),
    (roof_right, 'gold'),
    (bottom, 'saddlebrown')
]

vertices = []
faces = []
face_colors = []

for shape, color in all_faces:
    base_index = len(vertices)
    vertices.extend(shape)
    # Buat triangulasi manual (anggap semua segiempat & segitiga)
    if len(shape) == 3:
        faces.append([base_index, base_index + 1, base_index + 2])
        face_colors.append(color)
    elif len(shape) == 4:
        faces.append([base_index, base_index + 1, base_index + 2])
        faces.append([base_index, base_index + 2, base_index + 3])
        face_colors.extend([color, color])

x, y, z = zip(*vertices)
i, j, k = zip(*faces)

fig = go.Figure(data=[
    go.Mesh3d(
        x=x, y=y, z=z,
        i=i, j=j, k=k,
        facecolor=face_colors,
        flatshading=True,
        opacity=1.0,
    )
])

fig.update_layout(
    title='202310370311083_Reihandany_Rumah3D',
    scene=dict(
        xaxis=dict(visible=False),
        yaxis=dict(visible=False),
        zaxis=dict(visible=False),
        aspectratio=dict(x=1.5, y=1, z=1),
    )
)

fig.show(renderer="browser")
fig.write_html("rumah3d.html", full_html=True, include_plotlyjs='cdn')