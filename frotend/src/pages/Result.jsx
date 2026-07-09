
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
import LoadingSkeleton from "../components/LoadingSkeleton";


function Results() {


  const { analysis_id } = useParams()
  const [analysisData, setAnalysisData] = useState(null);
 useEffect(() => {
    const handleResult = async () => {
      try {
        const response = await fetchAnalyzeiedData(analysis_id);
        setAnalysisData(response);
      } catch (error) {
        console.error("Not fetched data:", error);
      }
    };

    if (analysis_id) {
      handleResult();
    }
  }, [analysis_id]);



    // -----------------------------
  // Loading State
  // -----------------------------
  // console.log("analysisData:", analysisData);
  // console.log(Object.keys(analysisData));
  // console.log("missing_skills:", analysisData?.missing_skills);

  
  if (!analysisData) {
    return (
      <div className="min-h-screen bg-gradient-to-br from-slate-50 via-blue-50 to-indigo-50">

        <DashboardNavbar />
<div className="mx-auto max-w-7xl animate-in fade-in duration-500 px-4 py-8 sm:px-6 lg:px-8">
          <LoadingSkeleton />
        </div>

      </div>
    );
  }

  // -----------------------------
  // Dashboard
  // -----------------------------

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-50 via-blue-50 to-indigo-50">
      <DashboardNavbar />
      
<div className="mx-auto max-w-7xl animate-in fade-in duration-500 px-4 py-8 sm:px-6 lg:px-8">

        {analysisData && (
          <>
            {/* Dashboard Header */}
            <DashboardHeader
              analysisId={analysis_id}
              atsScore={analysisData.ats_score}
            />

            <div className="space-y-6">

              {/* Row 1 */}
              <div className="grid grid-cols-1 gap-6 lg:grid-cols-4">

                <div className="lg:col-span-1">
                  <ATSScoreCard
                    atsScore={analysisData.ats_score}
                  />
                </div>

                <div className="lg:col-span-3">
                  <SummaryCard
                    summary={analysisData.summary}
                  />
                </div>

              </div>

              {/* Row 2 */}
              <TechnicalSkillsCard
                technicalSkills={analysisData.technical_skills}
              />

              {/* Row 3 */}
              <div className="grid grid-cols-1 gap-6 md:grid-cols-2">

                <SoftSkillsCard
                  softSkills={analysisData.soft_skills}
                />

                <MissingSkillsCard
                  missingSkills={analysisData.missing_skills}
                />

              </div>

              {/* Row 4 */}
              <SuggestionsCard
                suggestions={analysisData.suggestions}
              />

            </div>
          </>
        )}

      </div>
    </div>
  );
}

export default Results;