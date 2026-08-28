import "./InterviewPreparation.css";
import { fetchInterviewPrepration } from "../services/app";
import React, { useEffect, useState } from "react";
import { useParams, useNavigate } from "react-router-dom";


function InterviewPreparation() {
  const { role_id } = useParams();
  const navigate = useNavigate();
  const [error, setError] = useState(false);
  const [loading, setLoading] = useState(true);

  const [questions, setQuestions] = useState(null);
  const [selectedskill , setSelectedSkill] = useState(null)

  const [selectedDifficulty , setDifficulty ] = useState("")
  const [selectedQuestionType , setQuestionType ] = useState("")

 useEffect(() => {

  const loadQuestions = async () => {

    setLoading(false);
    setError(false);

    try {

      const data = await fetchInterviewPrepration(role_id);

      console.log("Interview Preparation API Response:", data);

      setQuestions(data);

    } catch (err) {

      console.error("Interview Preparation API Error:", err);

      setError(true);

    } finally {

      setLoading(false);

    }

  };

  loadQuestions();

}, [role_id]);

if (loading) {
  return (
    <div className="interview-preparation-page">
      <h2>🎯 Interview Preparation</h2>
      <p>Loading interview questions...</p>
    </div>
  );
}

if (error) {
  return (
    <div className="interview-preparation-page">

      <div className="error-state">

        <div className="error-icon">
          ⚠️
        </div>

        <h2>
          Unable to Load Interview Preparation
        </h2>

        <p>
          Something went wrong while loading your
          interview questions. Please try again.
        </p>

        <button onClick={() => window.location.reload()}>
          Try Again
        </button>

      </div>

    </div>
  );
}
  // -----------------------------
  // Preparation Overview
  // -----------------------------

  const questionList = questions?.questions || [];

 const filteredQuestions = questionList.filter((question) => {

  const skillMatch =
    !selectedskill || question.skill === selectedskill;

  const difficultyMatch =
    !selectedDifficulty ||
    question.difficulty === selectedDifficulty;

  const typeMatch =
    !selectedQuestionType ||
    question.question_type === selectedQuestionType;

  return skillMatch && difficultyMatch && typeMatch;
});


 
    const totalQuestions = questionList.length;

  const totalSkills = new Set(
    questionList.map((question) => question.skill)
  ).size;

  const totalDifficulties = new Set(
    questionList.map((question) => question.difficulty)
  ).size;

  // -----------------------------
  // Your Skills
  // -----------------------------

  const skills = [
    ...new Set(
      questionList.map((question) => question.skill)
    ),
  ];

  return (
    <div className="interview-preparation-page">

      {/* Page Header */}

      <header className="interview-header">

        <h1>🎯 Interview Preparation</h1>

        <p>
          Practice questions based on your resume skills
        </p>

      </header>


      {/* Preparation Overview */}

      <section className="preparation-overview">

        <h2>📊 Preparation Overview</h2>

        <div className="overview-stats">

          <div className="overview-item">
            <strong>{totalQuestions}</strong>
            <span>Total Questions</span>
          </div>

          <div className="overview-item">
            <strong>{totalSkills}</strong>
            <span>Total Skills</span>
          </div>

          <div className="overview-item">
            <strong>{totalDifficulties}</strong>
            <span>Difficulty Levels</span>
          </div>

        </div>

      </section>


      {/* Your Skills */}

      <section className="your-skills">

        <h2>🛠️ Your Skills</h2>

        <div className="skill-chips">


        {skills.map((skill) => (
          <button
            key={skill}
            className={`skill-chip ${
              selectedskill === skill ? "selected" : ""
            }`}
            onClick={() => setSelectedSkill(skill)}
          >
            {skill}
          </button>
        ))}

        </div>

      </section>


      {/* Interview Questions */}
<section className="interview-questions">

  

  <div className="questions-header">
    <h2>📝 Interview Questions</h2>

    <span>
  {questionList.length} Questions
    </span>
  </div>


  {/* Question Filters */}

  <div className="question-filters">

    {/* Skill Filter */}

    <div className="filter-group">

      <label>Skill</label>

      <select
        value={selectedskill || ""}
        onChange={(e) => setSelectedSkill(e.target.value)}
      >

        <option value="">
          All Skills
        </option>

        {skills.map((skill) => (
          <option
            key={skill}
            value={skill}
          >
            {skill}
          </option>
        ))}

      </select>

    </div>


    {/* Difficulty Filter */}

    <div className="filter-group">

      <label>Difficulty</label>

      <select
        value={selectedDifficulty}
        onChange={(e) => setDifficulty(e.target.value)}
      >

        <option value="">
          All Levels
        </option>

        <option value="Beginner">
          Beginner
        </option>

        <option value="Intermediate">
          Intermediate
        </option>

        <option value="Advanced">
          Advanced
        </option>

      </select>

    </div>


    {/* Question Type Filter */}

    <div className="filter-group">

      <label>
        Question Type
      </label>

      <select
        value={selectedQuestionType}
        onChange={(e) => setQuestionType(e.target.value)}
      >

        <option value="">
          All Types
        </option>

        <option value="Theory">
          Theory
        </option>

        <option value="Coding">
          Coding
        </option>

        <option value="MCQ">
          MCQ
        </option>

        <option value="Scenario">
          Scenario
        </option>

      </select>

    </div>


    {/* Clear Filters */}

    <button
      className="clear-filters"
      onClick={() => {

        setSelectedSkill(null);
        setDifficulty("");
        setQuestionType("");

      }}
    >
      Clear Filters
    </button>

  </div>



<div className="question-list">

  {filteredQuestions.length === 0 ? (

    <div className="empty-questions">

      <div className="empty-icon">
        🔍
      </div>

      <h3>
        No Questions Found
      </h3>

      <p>
        No interview questions match your selected filters.
      </p>

      <button
        className="clear-filters"
        onClick={() => {
          setSelectedSkill(null);
          setDifficulty("");
          setQuestionType("");
        }}
      >
        Clear Filters
      </button>

    </div>

  ) : (

    filteredQuestions.map((question) => (

      <div
        key={question.id}
        className="question-card"
      >

        <div className="question-card-header">

          <span className="question-skill">
            {question.skill}
          </span>

          <span className="question-difficulty">
            {question.difficulty}
          </span>

        </div>

        <p className="question-text">
          {question.question}
        </p>

        <div className="question-card-footer">

          <span className="question-type">
            {question.question_type}
          </span>

          <button
            onClick={() =>
              navigate(
                `/interview-preparation/${role_id}/question/${question.id}`
              )
            }
          >
            View →
          </button>

        </div>

      </div>

    ))

  )}

</div>

</section>

    </div>
  );
}

export default InterviewPreparation;