import { useState } from "react";
import { analyzedResume } from "../services/app";


function UploadPdf () {

    const[file , setFile] = useState(null)

    const handleAnalyse = async() =>{
        if (!file){
            alert("Please Select Pdf: ")
            return;
        }

    try{
        const response = analyzedResume(file)
          console.log(response)
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


            <button onClick={handleAnalyse}>
                Analyzed Resume
            </button>
        </div>
    )
}

export default UploadPdf