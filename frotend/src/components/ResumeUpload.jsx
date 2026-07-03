import { useState } from "react";
import { analyzedResume } from "../services/app";


function UploadPdf () {

    const[file , setFile] = useState(null)

    const[analysis , setAnalysis] = useState(null)

    const handleAnalyse = async() =>{
        if (!file){
            alert("Please Select Pdf: ")
            return;
        }

    try{
        const response = await analyzedResume(file)
          console.log(response)
          setAnalysis(response)
    }
    catch(error){
        console.error("Analysis failed:", error);    }  
    };
    

    return (
        <div>
            <input
            type="file"
            accept=".pdf"
            onChange={(e) => setFile(e.target.files[0])}

            />
            {
    analysis && (
        <div>
            <h3>Analyzed Resume</h3>

            <p>Resume ID: {analysis.resume_id}</p>

            <p>Analysis ID: {analysis.analysis_id}</p>
            <p>ATS Score: {analysis.ats_score}</p>

            <p>techncial skill:- {analysis.technical_skills}</p>
            <p>summary:-- {analysis.summary}</p>
            

            <p>{analysis.message}</p>
        </div>
    )
}
          

            <button onClick={handleAnalyse}>
                Analyzed Resume
            </button>
        </div>
    )
}

export default UploadPdf