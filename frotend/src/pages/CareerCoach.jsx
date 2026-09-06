import React from "react";
import "./CareerCoach.css";
import { useParams } from "react-router-dom";
import { useState , useEffect } from "react";
import ReactMarkdown from "react-markdown";

import {fetchCareerChatHistory , sendCareerChatMessage , clearCareerChat , fetchLearningProgress} from "../services/app"

function CareerCoach() {

  const { resume_id } = useParams();



  const [chatHistory, setChatHistory] = useState([]);
  const [ message , setMessage] = useState("")
  const[isloading, setIsLoading] = useState(false)
  const [chatError, setChatError] = useState("");
  const [progressData, setProgressData] = useState(null);


  const handleClearChat = async () => {
  try {
    setChatError("");

    await clearCareerChat(resume_id);

    setChatHistory([]);

    console.log("Career Chat cleared successfully");
  } catch (error) {
    console.error("Career Chat Clear API Error:", error);

    setChatError("Unable to clear your chat. Please try again.");
  }
};

 const handleSendMessage = async () => {
  if (!message.trim() || isloading) {
    return;
  }

  try {
    setIsLoading(true);
    setChatError("");

    const data = await sendCareerChatMessage(
      resume_id,
      message.trim()
    );

    console.log("Career Chat Send API Response:", data);

    setMessage("");
  } catch (error) {
    console.error("Career Chat Send API Error:", error);

    setChatError("Unable to send your message. Please try again.");
  } finally {
    setIsLoading(false);
  }
};



  const handleRetry = async () => {
  try {
    setChatError("");

    const data = await fetchCareerChatHistory(resume_id);

    console.log("Career Chat Retry Response:", data);

    setChatHistory(data.history || []);
  } catch (error) {
    console.error("Career Chat Retry Error:", error);

    setChatError("Unable to load your career chat.");
  }
};



 useEffect(() => {
  const loadChatHistory = async () => {
    try {
      setChatError("");

      const data = await fetchCareerChatHistory(resume_id);

      console.log("Career Chat History API Response:", data);

      setChatHistory(data.history || []);
    } catch (error) {
      console.error("Career Chat History API Error:", error);

      setChatError("Unable to load your career chat.");
    }
  };

  loadChatHistory();
}, [resume_id]);

useEffect(() => {
  const loadProgress = async () => {
    try {
      const data = await fetchLearningProgress(resume_id);

      console.log("Career Coach Learning Progress:", data);

      setProgressData(data);
    } catch (error) {
      console.error(
        "Career Coach Learning Progress API Error:",
        error
      );
    }
  };

  loadProgress();
}, [resume_id]);



  // ✅ return is INSIDE CareerCoach
  return (
    <div className="career-coach-page">

      {/* Header */}

      <header className="career-coach-header">

        <div className="career-coach-header-left">

          <div className="career-coach-icon">
            🤖
          </div>

          <div>

            <div className="career-coach-title-row">

              <h1>Career Coach</h1>

              <span className="ai-badge">
                AI Powered
              </span>

            </div>

            <p>
              Get personalized career guidance based on your
              resume, target role and learning journey.
            </p>

          </div>

        </div>

      </header>


{/* CC-12 Career Context */}

<div className="career-context">

  <div className="career-context-header">
    <div>
      <h2>Career Context</h2>
      <p>Your current career profile and learning status</p>
    </div>
  </div>

  <div className="career-context-grid">

    <div className="context-card">
      <div className="context-icon">
        🎯
      </div>

      <div className="context-info">
        <span className="context-label">
          Target Role
        </span>

        <strong className="context-value">
          Backend Developer
        </strong>
      </div>
    </div>


    <div className="context-card">
      <div className="context-icon">
        📈
      </div>

      <div className="context-info">
        <span className="context-label">
          Learning Progress
        </span>

        <strong className="context-value">
          {progressData?.progress || 0}%
        </strong>
      </div>
    </div>


    <div className="context-card">
      <div className="context-icon">
        📚
      </div>

      <div className="context-info">
        <span className="context-label">
          Current Learning Stage
        </span>

        <strong className="context-value">
          {progressData?.current_learning_stage || "Not started"}
        </strong>
      </div>
    </div>


    <div className="context-card">
      <div className="context-icon">
        ✅
      </div>

      <div className="context-info">
        <span className="context-label">
          Completed Skill
        </span>

        <strong className="context-value">
          {progressData?.completed_skill || "None yet"}
        </strong>
      </div>
    </div>

  </div>

</div>

      {/* Main */}

      <main className="career-coach-main">

        {/* Chat */}

        <section className="career-chat-panel">

          <div className="chat-panel-header">
            <span>Today</span>
          </div>


          {/* CC-04 Chat History */}

         <div className="chat-messages">


           {chatError ? (
    <div className="chat-error-state">
      <div className="chat-error-icon">
        ⚠️
      </div>

      <h3>Something went wrong</h3>

      <p>{chatError}</p>

      <button
        type="button"
        className="retry-button"
        onClick={handleRetry}
      >
        ↻ Retry
      </button>
    </div>
  ) : (
    <>
      {/* your existing CC-08 empty/history UI */}

      {isloading && (
        <div className="message-row ai-message-row">
          <div className="ai-avatar">
            🤖
          </div>

          <div className="ai-message ai-loading-message">
            <span className="typing-dot"></span>
            <span className="typing-dot"></span>
            <span className="typing-dot"></span>
          </div>
        </div>
      )}
    </>
  )}


  {chatHistory.length === 0 && !isloading ? (
    <div className="chat-empty-state">
      <div className="chat-empty-icon">
        💬
      </div>

      <h3>Start a conversation</h3>

      <p>
        Ask your Career Coach about your skills, learning path,
        career goals, or interview preparation.
      </p>

      <div className="empty-chat-suggestions">
        <span>💡 What should I learn next?</span>
        <span>🎯 How can I reach my target role?</span>
        <span>📚 What skills should I improve?</span>
      </div>
    </div>
  ) : (
    <>
      {chatHistory.map((chat, index) => (
        <React.Fragment key={chat.id || index}>

          <div className="message-row user-message-row">
            <div className="user-message">
              <p>{chat.user_message}</p>
            </div>

            <div className="user-avatar">
              GA
            </div>
          </div>

          <div className="message-row ai-message-row">
            <div className="ai-avatar">
              🤖
            </div>

           <div className="ai-message">
  <ReactMarkdown>
    {chat.ai_response}
  </ReactMarkdown>
</div>
          </div>

        </React.Fragment>
      ))}

      {isloading && (
        <div className="message-row ai-message-row">
          <div className="ai-avatar">
            🤖
          </div>

          <div className="ai-message ai-loading-message">
            <span className="typing-dot"></span>
            <span className="typing-dot"></span>
            <span className="typing-dot"></span>
          </div>
        </div>
      )}
    </>
  )}

</div>


          {/* Input */}

          <div className="career-chat-input">

            <button
            type="button"
            className= "attachment-button"
            title="Attach file"
>

              📎
            </button>

          <input
  type="text"
  className="chat-input"
  placeholder={
    isloading
      ? "Career Coach is thinking..."
      : "Ask your Career Coach anything..."
  }
  value={message}
  onChange={(e) => setMessage(e.target.value)}
  onKeyDown={(e) => {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();
      handleSendMessage();
    }
  }}
  disabled={isloading}
/>

            <button 
            type="button"
            className="send-button"
            onClick={handleSendMessage}
            disabled = {!message.trim() || isloading  }
            >
                {isloading ? "⏳" : "➤"}
            </button>

          </div>

        </section>


        {/* Right sidebar stays here */}


        {/* Right Sidebar */}

        <aside className="career-coach-sidebar">

          <button
            type="button"
            className="clear-chat-button"
            onClick={handleClearChat}
          >
            🗑️ Clear Chat
          </button>

        </aside>

      </main>

    </div>
  );

} // ✅ Close CareerCoach AFTER return


export default CareerCoach;