import { useNavigate } from "react-router-dom";
import "./Sidebar.css";

function Sidebar() {
  const navigate = useNavigate();

  return (
    <aside className="sidebar">

      <div className="sidebar-logo">
        ResumeAI
      </div>

      <nav className="sidebar-navigation">

        <button
          className="sidebar-item"
          onClick={() => navigate("/")}
        >
          📊 Dashboard
        </button>

        <button
          className="sidebar-item"
          onClick={() => navigate("/learning-resources")}
        >
          📚 Learning Resources
        </button>

      </nav>

    </aside>
  );
}

export default Sidebar;