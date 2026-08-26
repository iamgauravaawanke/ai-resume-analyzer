import React from "react";
import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";

import "./LearningResources.css";
import { fetchLearningResources } from "../services/app";

function LearningResources() {

  const { analysis_id } = useParams();

  const [resources, setResources] = useState(null);
  const [selectedSkill, setSelectedSkill] = useState(null);

  useEffect(() => {

    const loadResources = async () => {

      const data = await fetchLearningResources(analysis_id);

      console.log(
        "Learning Resources API Response:-",
        data
      );

      setResources(data);
    };

    loadResources();

  }, [analysis_id]);


  // Find the resource group for the selected skill
  const selectedResource = resources?.resources?.find(
    (resource) => resource.skill === selectedSkill
  );


  return (
    <div className="learning-resources-page">

      {/* Header */}
      <header className="learning-resources-header">

        <div className="header-icon">
          📚
        </div>

        <div>
          <h1>Learning Resources</h1>

          <p>
            Personalized resources based on your resume analysis.
          </p>
        </div>

      </header>


      {/* Recommended Skills */}
      <section className="recommended-skills">

        <h2>
          Your Recommended Skills
        </h2>

        <div className="skill-chips">

          {resources?.resources?.map((resource) => (

            <button
              key={resource.skill}
              className={`skill-chip ${
                selectedSkill === resource.skill
                  ? "selected"
                  : ""
              }`}
              onClick={() =>
                setSelectedSkill(resource.skill)
              }
            >
              {resource.skill}
            </button>

          ))}

        </div>

      </section>


      {/* Resources */}
      <section className="resources-section">

        <h2>
          Resources for {selectedSkill}
        </h2>

        <div className="resource-list">

          {selectedResource?.resources?.map((resource) => (

            <div
              className="resource-card"
              key={resource.title}
            >

              <div className="resource-info">

                <h3>
                  {resource.resource_type === "VIDEO"
                    ? "▶️"
                    : "📘"
                  }{" "}
                  {resource.title}
                </h3>

                <span className="resource-type">
                  {resource.resource_type}
                </span>

              </div>


              <button className="resource-action">
                Open Resource →
              </button>

            </div>

          ))}

        </div>

      </section>

    </div>
  );
}

export default LearningResources;