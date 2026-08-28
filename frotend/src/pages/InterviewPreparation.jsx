import "./InterviewPreparation.css";
import { fetchInterviewPrepration } from "../services/app";
import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";

function InterviewPreparation() {
  const { role_id } = useParams();

  const [questions, setQuestions] = useState(null);
  const [selectedskill , setSelectedSkill] = useState(null)

  const [selectedDifficulty , setDifficulty ] = useState("")
  const [selectedQuestionType , setQuestionType ] = useState("")

  useEffect(() => {
    const loadQuestions = async () => {
      const data = await fetchInterviewPrepration(role_id);

      console.log("Interview Preparation API Response:", data);

      setQuestions(data);
    };

    loadQuestions();
  }, [role_id]);

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

  <div className="question-list">

    {filteredQuestions.map((question) => (

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

        <span className="question-type">
          {question.question_type}
        </span>

      </div>

    ))}

  </div>

</section>

    </div>
  );
}

export default InterviewPreparation;