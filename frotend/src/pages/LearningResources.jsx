import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";

import "./LearningResources.css";
import { fetchLearningResources } from "../services/app";

function LearningResources() {

  const { analysis_id } = useParams();

  const [resources, setResources] = useState(null);
  const [selectedSkill, setSelectedSkill] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  const loadResources = async () => {

    setLoading(true);
    setError(null);

    try {

      const data = await fetchLearningResources(analysis_id);

      console.log(
        "Learning Resources API Response:",
        data
      );

      setResources(data);

    } catch (err) {

      console.error(
        "Learning Resources API Error:",
        err
      );

      setError(
        "Something went wrong while loading your learning resources."
      );

    } finally {

      setLoading(false);

    }
  };

  useEffect(() => {
    loadResources();
  }, [analysis_id]);


  // Automatically select first skill
  useEffect(() => {

    if (
      resources?.resources?.length > 0 &&
      !selectedSkill
    ) {
      setSelectedSkill(
        resources.resources[0].skill
      );
    }

  }, [resources, selectedSkill]);


  // -------------------------
  // Loading
  // -------------------------

  if (loading) {

    return (
      <div className="learning-resources-page">

        <div className="learning-container">

          <div className="skeleton-header">
            <div className="skeleton-icon"></div>

            <div>
              <div className="skeleton-title"></div>
              <div className="skeleton-subtitle"></div>
            </div>
          </div>


          <div className="skeleton-section">

            <div className="skeleton-heading"></div>

            <div className="skeleton-skills">
              <div></div>
              <div></div>
              <div></div>
            </div>

          </div>


          <div className="skeleton-card"></div>
          <div className="skeleton-card"></div>

        </div>

      </div>
    );
  }


  // -------------------------
  // Error
  // -------------------------

  if (error) {

    return (
      <div className="learning-resources-page">

        <div className="learning-container">

          <div className="error-state">

            <div className="error-icon">
              ⚠️
            </div>

            <h2>
              Failed to Load Resources
            </h2>

            <p>
              {error}
            </p>

            <button
              className="retry-button"
              onClick={loadResources}
            >
              Try Again
            </button>

          </div>

        </div>

      </div>
    );
  }


  // -------------------------
  // No recommended skills
  // -------------------------

  if (!resources?.resources?.length) {

    return (
      <div className="learning-resources-page">

        <div className="learning-container">

          <div className="empty-state">

            <div className="empty-icon">
              📚
            </div>

            <h2>
              No Learning Resources Yet
            </h2>

            <p>
              We couldn't find any recommended
              learning resources for your analysis.
            </p>

          </div>

        </div>

      </div>
    );
  }


  // -------------------------
  // Selected skill
  // -------------------------

  const selectedResource =
    resources.resources.find(
      (resource) =>
        resource.skill === selectedSkill
    );


  const selectedResources =
    selectedResource?.resources || [];


  // -------------------------
  // Main UI
  // -------------------------

  return (

    <div className="learning-resources-page">

      <div className="learning-container">


        {/* HEADER */}

        <header className="learning-header">

          <div className="header-icon">
            📚
          </div>

          <div>

            <h1>
              Learning Resources
            </h1>

            <p>
              Personalized resources based on your
              resume analysis.
            </p>

          </div>

        </header>


        {/* PERSONALIZED BANNER */}

        <section className="learning-banner">

          <div className="banner-icon">
            🎯
          </div>

          <div>

            <h3>
              Personalized Learning
            </h3>

            <p>
              Resources selected based on the skills
              identified in your resume analysis.
            </p>

          </div>

          <div className="skill-count">

            <strong>
              {resources.resources.length}
            </strong>

            <span>
              Recommended Skills
            </span>

          </div>

        </section>


        {/* SKILLS */}

        <section className="skills-section">

          <div className="section-heading">

            <div>
              <h2>
                Your Recommended Skills
              </h2>

              <p>
                Select a skill to explore learning resources.
              </p>
            </div>

          </div>


          <div className="skill-chips">

            {resources.resources.map((resource) => (

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

                <span className="skill-dot"></span>

                {resource.skill}

              </button>

            ))}

          </div>

        </section>


        {/* RESOURCES */}

        <section className="resources-section">

          <div className="resources-heading">

            <div>

              <h2>
                Resources for {selectedSkill}
              </h2>

              <p>
                Explore curated resources to strengthen
                this skill.
              </p>

            </div>

            <div className="resource-count">

              {selectedResources.length} Resources

            </div>

          </div>


          {/* No resources for selected skill */}

          {selectedResources.length === 0 ? (

            <div className="skill-empty-state">

              <div className="skill-empty-icon">
                📚
              </div>

              <h3>
                Resources for {selectedSkill}
              </h3>

              <p>
                {selectedResource?.message ||
                  `Learning resources for ${selectedSkill} are not available yet.`}
              </p>

            </div>

          ) : (

            <div className="resource-list">

              {selectedResources.map((resource) => (

                <article
                  className="resource-card"
                  key={resource.url}
                >

                  <div className="resource-card-left">

                    <div className="resource-icon">

                      {resource.resource_type === "VIDEO"
                        ? "▶️"
                        : resource.resource_type === "GITHUB"
                        ? "💻"
                        : resource.resource_type === "COURSE"
                        ? "🎓"
                        : resource.resource_type === "ARTICLE"
                        ? "📖"
                        : "📘"}

                    </div>


                    <div className="resource-info">

                      <h3>
                        {resource.title}
                      </h3>

                      <span className="resource-type">
                        {resource.resource_type}
                      </span>

                    </div>

                  </div>


                  <a
                    className="resource-action"
                    href={resource.url}
                    target="_blank"
                    rel="noopener noreferrer"
                  >

                    {resource.resource_type === "VIDEO"
                      ? "Watch Video"
                      : "Open Resource"}

                    <span>
                      →
                    </span>

                  </a>

                </article>

              ))}

            </div>

          )}

        </section>

      </div>

    </div>
  );
}

export default LearningResources;