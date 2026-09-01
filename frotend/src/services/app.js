export const analyzedResume = async (file, role_id) => {
  const formData = new FormData();

  formData.append("file", file);
  formData.append("role_id", role_id);

  const response = await fetch(
    "http://127.0.0.1:8000/upload",
    {
      method: "POST",
      body: formData,
    }
  );

  return response.json();
};




export const fetchAnalyzeiedData = async (analysis_id) => {

  const response = await fetch(
    `http://127.0.0.1:8000/analysis/${analysis_id}`
  );

  const data = await response.json();

  console.log("FULL ANALYSIS DATA:", data);

  return data;
};

export const fetchRoles = async () => {
  const response = await fetch(
    "http://127.0.0.1:8000/roles"
  );

  const data = await response.json();

  return data;
};


export const fetchLearningResources = async (analysis_id) => {

    const response = await fetch(
        `http://127.0.0.1:8000/learning_Resources/${analysis_id}`
    );

    

    const data = await response.json();

    return data;
};



export const fetchInterviewPrepration = async (role_id) => {

    const response = await fetch(
        `http://127.0.0.1:8000/interview-preparation/${role_id}`
    );
 
    const data = await response.json();

    return data;
};

export const fetchLearningProgress = async (resume_id) => {
  const response = await fetch(
    `http://127.0.0.1:8000/progress_tracking/${resume_id}`
  );

  const data = await response.json();

  return data;
};


export const updateLearningProgress = async (
  resume_id,
  progress,
  completed_skill,
  current_learning_stage
) => {

  const response = await fetch(
    `http://127.0.0.1:8000/progress_tracking/${resume_id}?progress=${encodeURIComponent(progress)}&completed_skill=${encodeURIComponent(completed_skill)}&current_learning_stage=${encodeURIComponent(current_learning_stage)}`,
    {
      method: "PUT",
    }
  );

  const data = await response.json();

  return data;
};


export const resetLearningProgress = async (resume_id) => {

  const response = await fetch(
    `http://127.0.0.1:8000/progress-tracking/${resume_id}/reset`,
    {
      method: "POST",
    }
  );

  const data = await response.json();

  return data;
};