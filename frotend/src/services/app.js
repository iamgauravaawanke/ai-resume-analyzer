export const analyzedResume = async(file) => {
    const formData = new FormData()
    formData.append("file" , file)


    const response = await fetch('http://127.0.0.1:8000/upload', {
        method:"POST",
        body:formData

    }   )
    // console.log(response.data)

    return response.json()
}







export const fetchAnalyzeiedData = async (analysis_id) => {

    const response = await fetch(`http://127.0.0.1:8000/analysis/${analysis_id}`)


    const data = await response.json()

    return data 
   
}




export const fetchLearningResources = async (analysis_id) => {

    const response = await fetch(
        `http://127.0.0.1:8000/learning_Resources/${analysis_id}`
    );

    const data = await response.json();

    return data;
};