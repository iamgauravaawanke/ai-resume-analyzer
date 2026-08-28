import { useNavigate } from "react-router-dom";
import "./Sidebar.css";

function Sidebar({analysis_id , role_id}) {
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
          onClick={() => navigate(`/learning-resources/${analysis_id}`)}
        >
          📚 Learning Resources
        </button>

        <button
          className="sidebar-item"
          onClick={() => navigate(`/interview-preparation/${role_id}`)}
        >
          📚 Interview Prepration
        </button>

      </nav>

    </aside>
  );
}

export default Sidebar;