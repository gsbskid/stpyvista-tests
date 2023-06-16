import streamlit as st
import pyvista as pv
from stpyvista import stpyvista
import pickle

st.set_page_config(page_icon="🧊", layout="wide")
pv.start_xvfb()


@st.cache_data
def get_cow(cow="cow"):
    with open("assets/cow.pkl", "rb") as f:
        cow = pickle.load(f)
    return cow


# Add some styling with CSS selectors
with open("assets/style.css") as f:
    st.markdown(f"""<style>{f.read()}</style>""", unsafe_allow_html=True)

# Add badges to sidebar
with st.sidebar:
    with open("assets/badges.md") as f:
        st.markdown(f"""{f.read()}""", unsafe_allow_html=True)

st.title("🧊 `stpyvista`")
st.header("Show PyVista 3D visualizations in Streamlit")

cols = st.columns([1, 1])

with cols[0]:
    st.markdown(
        """
    `stpyvista` is a simple component that takes a PyVista plotter object and shows 
    it on Streamlit as an interactive element (as in it can be zoomed in/out, moved 
    and rotated, but the visualization state is not returned).
    It uses PyVista's [panel backend](https://docs.pyvista.org/user-guide/jupyter/panel.html) 
    for taking the plotter, [exports it to HTML](https://panel.holoviz.org/reference/panes/VTK.html) 
    and displays that within an iframe.

    **👈 List of demos:**

    - 🔑   Pass a key to avoid model re-rendering
    - 🍞   Textures and physically based rendering (PBR) [Not working]
    - 📤   Display your own STL file

    ****
    """,
        unsafe_allow_html=True,
    )

with cols[1]:
    cow = get_cow()

    plotter = pv.Plotter(window_size=[400, 300])

    plotter.add_mesh(cow, color="#babab2", pbr=True, metallic=0.05)

    plane = pv.Plane(center=[0, -3.65, 0], direction=[0, 1, 0], i_size=12, j_size=12)
    plane.point_data.clear()
    plotter.add_mesh(plane, color="#09ab3b", show_edges=True)
    plotter.background_color = "white"
    plotter.view_xy()
    plotter.camera.zoom(3.0)
    stpyvista(plotter, horizontal_align="left")

with st.expander("🛠️ Installation"):
    """
    ```sh
    pip install stpyvista
    ```
    """

with st.expander("✨ Use example", expanded=True):
    with st.echo():
        import streamlit as st
        import pyvista as pv
        from stpyvista import stpyvista

        ## Initialize a plotter object
        plotter = pv.Plotter(window_size=[400, 400])

        ## Create a mesh with a cube
        mesh = pv.Cube(center=(0, 0, 0))

        ## Add some scalar field associated to the mesh
        mesh["myscalar"] = mesh.points[:, 2] * mesh.points[:, 0]

        ## Add mesh to the plotter
        plotter.add_mesh(mesh, scalars="myscalar", cmap="bwr", line_width=1)

        ## Final touches
        plotter.background_color = "white"
        plotter.view_isometric()

        ## Pass a key to avoid re-rendering at each time something changes in the page
        stpyvista(plotter, key="pv_cube")

with st.expander("🔡 Also check:"):
    """
    * The PyVista project at [https://www.pyvista.org/](https://www.pyvista.org/)
    * @blackary['s blog post](https://blog.streamlit.io/how-to-build-your-own-streamlit-component/) on how to build a custom component
    * [Post](https://discuss.streamlit.io/t/stpyvista-show-pyvista-3d-visualizations-in-streamlit/31802) on streamlit discuss forum.

    """

r"""
*****
Current version **0.0.8**
"""
