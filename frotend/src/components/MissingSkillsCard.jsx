import { Card, CardContent } from "../components/ui/card";
import { AlertTriangle } from "lucide-react";

function MissingSkillsCard({ missingSkills = [] }) {
  return (
    <Card className="rounded-3xl shadow-lg transition-all duration-300 hover:-translate-y-1 hover:shadow-2xl">
      <CardContent className="p-8">

        <div className="flex items-center gap-3">

          <div className="rounded-xl bg-red-100 p-3">
            <AlertTriangle className="h-6 w-6 text-red-600" />
          </div>

          <div>
            <h2 className="text-2xl font-bold text-gray-900">
              Missing Skills
            </h2>

            <p className="text-sm text-gray-500">
              Skills recommended to improve your resume
            </p>
          </div>

        </div>

        <div className="mt-6 flex flex-wrap gap-3">

          {missingSkills?.length > 0 ? (
            missingSkills.map((skill, index) => (
              <span
                key={index}
                className="rounded-full bg-red-100 px-4 py-2 text-sm font-semibold text-red-700 transition hover:bg-red-600 hover:text-white"
              >
                {skill}
              </span>
            ))
          ) : (
            <div className="w-full rounded-xl bg-green-50 p-6 text-center">
              <p className="font-medium text-green-600">
                🎉 No missing skills detected.
              </p>
            </div>
          )}

        </div>

      </CardContent>
    </Card>
  );
}

export default MissingSkillsCard;