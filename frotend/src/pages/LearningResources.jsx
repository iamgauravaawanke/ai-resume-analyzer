import React from "react";
import "./LearningResources.css";


const recommendedSkills = ["Docker", "AWS", "PyTorch", "Git"];

const resources = [
  {
    title: "Docker Official Documentation",
    type: "DOCUMENTATION",
    action: "Open Resource",
  },
  {
    title: "Docker Tutorial",
    type: "VIDEO",
    action: "Watch Video",
  },
];

function LearningResources() {
  return (
    <div className="learning-resources-page">

      {/* Header */}
      <header className="learning-resources-header">
        <div className="header-icon">📚</div>

        <div>
          <h1>Learning Resources</h1>
          <p>
            Personalized resources based on your resume analysis.
          </p>
        </div>
      </header>

      {/* Recommended Skills */}
      <section className="recommended-skills">
        <h2>Your Recommended Skills</h2>

        <div className="skill-chips">
          {recommendedSkills.map((skill) => (
            <button
              key={skill}
              className="skill-chip"
            >
              {skill}
            </button>
          ))}
        </div>
      </section>

      {/* Resources */}
      <section className="resources-section">
        <h2>Resources for Docker</h2>

        <div className="resource-list">

          {resources.map((resource) => (
            <div
              className="resource-card"
              key={resource.title}
            >
              <div className="resource-info">

                <h3>
                  {resource.type === "VIDEO" ? "▶️" : "📘"}{" "}
                  {resource.title}
                </h3>

                <span className="resource-type">
                  {resource.type}
                </span>

              </div>

              <button className="resource-action">
                {resource.action}
              </button>
            </div>
          ))}

        </div>
      </section>

    </div>
  );
}

export default LearningResources;