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

    const response = await fetch(`http://127.0.0.1:8000/analysis/${analysis_id}`)


    const data = await response.json()

    return data 
   
}


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

