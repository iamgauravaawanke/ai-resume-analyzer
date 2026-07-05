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
            <h1>hello </h1>
        </div>
    )
}
export default UploadPdf