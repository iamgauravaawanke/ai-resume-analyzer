
import { useParams } from "react-router-dom";
import { fetchAnalyzeiedData } from "../services/app";
import { useEffect, useState } from "react";
import ATSScoreCard from "../components/ATSScoreCard"
import SummaryCard from "../components/SummaryCard"
import TechnicalSkillsCard from "../components/TechnicalSkillsCard";
import SoftSkillsCard from "../components/SoftSkillsCard";
import MissingSkillsCard from "../components/MissingSkillsCard";
import SuggestionsCard from "../components/SuggestionsCard";
import DashboardNavbar from "../components/DashboardNavbar";
import DashboardHeader from "../components/DashboardHeader";
function Results() {


  const { analysis_id } = useParams()
  const [analysisData, setAnalysisData] = useState(null);
  
  useEffect(  ()=>{
    const handleResult = async() =>{
      try{
        const response = await fetchAnalyzeiedData(analysis_id)
        setAnalysisData(response)

      
      }
      catch(error){
        console.error("not fetched data", error);

      }  
    }

  if (analysis_id) {
    handleResult();
  }  
  }, [analysis_id])

  return (




<div className="min-h-screen bg-gradient-to-br from-slate-50 via-blue-50 to-indigo-50">

  <DashboardNavbar />

  <div className="mx-auto max-w-7xl px-6 py-10">

    {/* Dashboard Heading */}

    <div className="mb-10">
      <h1 className="text-4xl font-bold">
        Resume Analysis Dashboard
      </h1>

      <p className="mt-2 text-gray-500">
        AI-powered insights for your uploaded resume.
      </p>
    </div>

    {/* Row 1 */}
    {analysisData && (
      <div className="grid grid-cols-1 gap-6 lg:grid-cols-4">

        <div className="lg:col-span-1">
          <ATSScoreCard atsScore={analysisData.ats_score} />
        </div>

        <div className="lg:col-span-3">
          <SummaryCard summary={analysisData.summary} />
        </div>

      </div>
    )}

    {/* Row 2 */}
    {analysisData && (
      <div className="mt-6">
        <TechnicalSkillsCard
          technicalSkills={analysisData.technical_skills}
        />
      </div>
    )}

    {/* Row 3 */}
    {analysisData && (
      <div className="mt-6 grid grid-cols-1 gap-6 md:grid-cols-2">

        <SoftSkillsCard
          softSkills={analysisData.soft_skills}
        />

        <MissingSkillsCard
          missingSkills={analysisData.missing_skills}
        />

      </div>
    )}

    {/* Row 4 */}
    {analysisData && (
      <div className="mt-6">
        <SuggestionsCard
          suggestions={analysisData.suggestions}
        />
      </div>
    )}

  </div>

</div>
  );
}

export default Results;