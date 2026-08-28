import React, { useEffect, useState } from "react";
import { useParams, useNavigate } from "react-router-dom";
import { fetchInterviewPrepration } from "../services/app";
import "./InterviewQuestion.css";

function InterviewQuestion() {

  const { role_id, question_id } = useParams();

  const navigate = useNavigate();

  const [questions, setQuestions] = useState([])
  const [loading, setLoading] = useState(true);

 
  useEffect(() => {

    const loadQuestions = async () => {

      const data = await fetchInterviewPrepration(role_id);

      setQuestions(data.questions || []);
       setLoading(false)

    };

    loadQuestions();
   

  }, [role_id]);

if (loading) {
  return (
    <div className="interview-question-page">
      <h2>🎯 Interview Question</h2>
      <p>Loading question...</p>
    </div>
  );
}


  // Find current question position
  const questionIndex = questions.findIndex(
    (item) => item.id === Number(question_id)
  );


  // Current question
  const question = questions[questionIndex];


  // Previous and Next questions
  const previousQuestion = questions[questionIndex - 1];

  const nextQuestion = questions[questionIndex + 1];


  if (!question) {
    return <div>Question not found.</div>;
  }


  return (
  <div className="interview-question-page">

  <button
    className="back-button"
    onClick={() =>
      navigate(`/interview-preparation/${role_id}`)
    }
  >
    ← Back to Interview Questions
  </button>

  <header className="interview-question-header">

    <h1>🎯 Interview Question</h1>

    <p>
      Test your knowledge and prepare for your interview.
    </p>

  </header>

  <div className="question-detail-card">

    <h2>
      {question.skill}
    </h2>

    <div className="question-meta">

      <span>
        {question.difficulty}
      </span>

      <span>
        {question.question_type}
      </span>

    </div>

    <p className="question-detail-text">
      {question.question}
    </p>

  </div>

  <p className="question-number">
    Question {questionIndex + 1} of {questions.length}
  </p>

  <div className="question-navigation">

    <button
      disabled={!previousQuestion}
      onClick={() =>
        navigate(
          `/interview-preparation/${role_id}/question/${previousQuestion.id}`
        )
      }
    >
      ← Previous
    </button>

    <button
      disabled={!nextQuestion}
      onClick={() =>
        navigate(
          `/interview-preparation/${role_id}/question/${nextQuestion.id}`
        )
      }
    >
      Next →
    </button>

  </div>

</div>
  );
}

export default InterviewQuestion;