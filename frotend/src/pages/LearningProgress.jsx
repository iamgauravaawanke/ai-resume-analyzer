import React, { useEffect, useState } from "react";
import "./LearningProgress.css";
import { fetchLearningProgress ,
   updateLearningProgress,
   resetLearningProgress,

} from "../services/app";
import { useParams } from "react-router-dom";
import { progress } from "framer-motion";

function LearningProgress() {

  const { resume_id } = useParams();

  const [progressData, setProgressData] = useState(null);

  const [updateProgress, setUpdateProgress] = useState("")
  const [updateskill , setUpdateSkill] = useState("")
  const [updatestage , setUpdateStage ] = useState("") 
  const [showUpdateForm, setShowUpdateForm] = useState(false);

  useEffect(() => {

    const loadProgress = async () => {

      const data = await fetchLearningProgress(resume_id);

      console.log("Learning Progress API Response:", data);

      setProgressData(data);

    };

    loadProgress();

  }, [resume_id]);


  const handleUpdateProgres = async () => {

    try {
      const data = await updateLearningProgress(
     resume_id,
  updateProgress,
  updateskill,
  updatestage
    ) 
      
      console.log("Update Learning Progress" , data )

      setProgressData(data)
      
      setShowUpdateForm(false)
      }
    catch (error) {

      console.error("Update Learning Progress Error:" , error)
    }
  };
  const handleResetProgress = async () => {

    const confirmed = window.confirm(
      "Are you sure you want to reset your learning progress?"
    );

    if (!confirmed) {
      return;
    }

    try {

      const data = await resetLearningProgress(resume_id);

      console.log("Reset Learning Progress:", data);

      setProgressData(data);

    } catch (error) {

      console.error("Reset Learning Progress Error:", error);

    }z
  };

  return (
    <div className="learning-progress-page">

      {/* Header */}

      <header className="learning-progress-header">

        <div className="header-icon">
          📈
        </div>

        <div>

          <h1>
            Learning Progress
          </h1>

          <p>
            Track your learning journey and skill completion.
          </p>

        </div>

      </header>


      {/* Overall Progress */}

<section className="overall-progress">

  <h2>Overall Progress</h2>

  <div className="progress-circle">

    <strong>
      {progressData?.progress || 0}%
    </strong>

    <span>
      Overall Progress
    </span>

  </div>

  <div className="progress-bar">

    <div
      className="progress-fill"
      style={{
        width: `${progressData?.progress || 0}%`
      }}
    />

  </div>

  <p className="progress-message">
    {progressData?.progress >= 75
      ? "Great progress!"
      : "Keep going! You're making progress."}
  </p>

</section>


      {/* Completed Skill */}

      <section className="progress-card">

        <h2>
          Completed Skill
        </h2>

        <div className="progress-value">
  {progressData?.completed_skill
    ? `✅ ${progressData.completed_skill}`
    : "No skill completed yet"}
</div>

      </section>


      {/* Current Learning Stage */}

      <section className="progress-card">

        <h2>
          Current Learning Stage
        </h2>

      <div className="progress-value">
  {progressData?.current_learning_stage
    ? `📚 ${progressData.current_learning_stage}`
    : "Not started"}
</div>

      </section>


      {/* Reset Button */}

      <section className="reset-progress">
  
<button onClick={() => setShowUpdateForm(true)}>
  Update Progress
</button>


 
        <button onClick={handleResetProgress}   >
          Reset Progress
        </button>

    {showUpdateForm && (
  <section className="update-progress-form">

    <h2>Update Learning Progress</h2>

    <label>
      Progress
    </label>

  <input
  type="number"
  min="0"
  max="100"
  value={updateProgress}
  onChange={(e) => setUpdateProgress(e.target.value)}
  placeholder="Enter progress"
/>

    <label>
      Completed Skill
    </label>

  <input
  type="text"
  value={updateskill}
  onChange={(e) => setUpdateSkill(e.target.value)}
  placeholder="e.g. Python"
/>

    <label>
      Current Learning Stage
    </label>

<input
  type="text"
  value={updatestage}
  onChange={(e) => setUpdateStage(e.target.value)}
  placeholder="e.g. Python"
/>

    <button  onClick={handleUpdateProgres }>
      Save Progress
    </button>

    <button
      onClick={() => setShowUpdateForm(false)}
    >
      Cancel
    </button>

  </section>
)}
    

      </section>

    </div>
  );
}

export default LearningProgress;