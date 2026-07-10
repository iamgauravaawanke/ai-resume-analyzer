
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
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
  const handleResult = async () => {
    setLoading(true);
    setError(null);

    try {
      const response = await fetchAnalyzeiedData(analysis_id);

      setAnalysisData(response);
    } catch (err) {
      console.error("Not fetched data:", err);

      setError("Failed to load resume analysis.");
    } finally {
      setLoading(false);
    }
  };

  if (analysis_id) {
    handleResult();
  }
}, [analysis_id]);



useEffect(() => {
  const handleResult = async () => {
    setLoading(true);
    setError(null);

    try {
      const response = await fetchAnalyzeiedData(analysis_id);

      setAnalysisData(response);
    } catch (err) {
      console.error("Not fetched data:", err);

      setError("Failed to load resume analysis.");
    } finally {
      setLoading(false);
    }
  };

  if (analysis_id) {
    handleResult();
  }
}, [analysis_id]);


if (loading) {
  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-50 via-blue-50 to-indigo-50">
      <DashboardNavbar />

      <div className="mx-auto max-w-7xl animate-in fade-in duration-500 px-4 py-8 sm:px-6 lg:px-8">
        <LoadingSkeleton />
      </div>
    </div>
  );
}
console.log("Suggestions:", analysisData.suggestions);// -----------------------------
// Error State
// -----------------------------
if (error) {
  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-50 via-blue-50 to-indigo-50">
      <DashboardNavbar />

      <div className="flex min-h-[80vh] items-center justify-center px-4">
        <div className="max-w-md rounded-3xl bg-white p-10 text-center shadow-xl">

          <h2 className="text-3xl font-bold text-red-600">
            Failed to Load Analysis
          </h2>

          <p className="mt-4 text-gray-600">
            {error}
          </p>

        </div>
      </div>
    </div>
  );
}
console.log("analysisData =", analysisData);
console.log("analysisData.suggestions =", analysisData?.suggestions);
console.log("Is Array =", Array.isArray(analysisData?.suggestions));
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

            <div className="space-y-8">

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