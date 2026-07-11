import { Card, CardContent } from "../components/ui/card";
import { Code2 } from "lucide-react";

function TechnicalSkillsCard({ technicalSkills }) {
  
  return (
    <Card className="rounded-3xl border border-slate-200 shadow-md transition-all duration-300 hover:-translate-y-2 hover:shadow-2xl hover:border-blue-300">
      <CardContent className="p-8">
        {/* Header */}
        <div className="flex items-center gap-3">
          <div className="rounded-xl bg-blue-100 p-3">
            <Code2 className="h-6 w-6 text-blue-600" />
          </div>

          <div>
            <h2 className="text-2xl font-bold text-gray-900">
              Technical Skills
            </h2>

            <p className="text-sm text-gray-500">
              Technologies detected from your resume
            </p>
          </div>
        </div>

        {/* Skills */}
        <div className="mt-6 flex flex-wrap gap-3">
          {technicalSkills?.length > 0 ? (
            technicalSkills.map((skill, index) => (
              <span
                key={index}
                className="rounded-full bg-blue-100 px-4 py-2 text-sm font-semibold text-blue-700 transition hover:bg-blue-600 hover:text-white"
              >
                {skill}
              </span>
            ))
          ) : (
            <div className="w-full rounded-2xl border border-dashed border-slate-300 bg-slate-50 p-6 text-center">
              <p className="text-gray-500">
                No technical skills were detected.
              </p>
            </div>
          )}
        </div>
      </CardContent>
    </Card>
  );
}

export default TechnicalSkillsCard;