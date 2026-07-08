import { FileCheck2 } from "lucide-react";

function DashboardHeader({ analysisId, atsScore }) {
  return (
    <div className="mb-10 rounded-3xl bg-white p-8 shadow-lg">

      <div className="flex flex-col justify-between gap-6 md:flex-row md:items-center">

        {/* Left Side */}
        <div>

          <div className="flex items-center gap-3">

            <div className="rounded-xl bg-blue-100 p-3">
              <FileCheck2 className="h-7 w-7 text-blue-600" />
            </div>

            <div>
              <h1 className="text-4xl font-bold text-slate-900">
                Resume Analysis Dashboard
              </h1>

              <p className="mt-2 text-gray-500">
                AI-powered insights generated from your uploaded resume.
              </p>
            </div>

          </div>

        </div>

        {/* Right Side */}

        <div className="flex gap-4">

          <div className="rounded-2xl bg-slate-100 px-6 py-4 text-center">

            <p className="text-sm text-gray-500">
              Analysis ID
            </p>

            <h2 className="text-2xl font-bold">
              {analysisId}
            </h2>

          </div>

          <div className="rounded-2xl bg-blue-600 px-6 py-4 text-center text-white">

            <p className="text-sm">
              ATS Score
            </p>

            <h2 className="text-2xl font-bold">
              {atsScore}
            </h2>

          </div>

        </div>

      </div>

    </div>
  );
}

export default DashboardHeader;