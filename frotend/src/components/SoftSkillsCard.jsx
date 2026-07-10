import { Card, CardContent } from "../components/ui/card";
import { Users } from "lucide-react";

function SoftSkillsCard({ softSkills }) {



  const validSoftSkills = softSkills.filter(
    (skill) => skill && skill.trim() !== ""
  );

  return (
    <Card className="rounded-3xl shadow-lg transition-all duration-300 hover:-translate-y-1 hover:shadow-2xl">
      <CardContent className="p-8">

        {/* Header */}
        <div className="flex items-center gap-3">
          <div className="rounded-xl bg-green-100 p-3">
            <Users className="h-6 w-6 text-green-600" />
          </div>

          <div>
            <h2 className="text-2xl font-bold text-gray-900">
              Soft Skills
            </h2>

            <p className="text-sm text-gray-500">
              Professional strengths identified by AI
            </p>
          </div>
        </div>

        {/* Skills */}
        <div className="mt-6 flex flex-wrap gap-3">


           {validSoftSkills.length > 0 ? (

            validSoftSkills.map((skill, index) => (
              <span
                key={index}
                className="rounded-full bg-red-100 px-4 py-2 text-sm font-semibold text-red-700 transition-all duration-300 hover:scale-105 hover:bg-red-600 hover:text-white"
              >
                {skill}
              </span>
            ))

          ) : (

            <div className="w-full rounded-2xl border border-green-200 bg-green-50 p-6 text-center">

              <h3 className="text-lg font-semibold text-green-700">
                🎉 Great Job!
              </h3>

              <p className="mt-2 text-gray-600">
                No soft skills were detected.
              </p>
            </div>
          )}
        </div>

      </CardContent>
    </Card>
  );
}

export default SoftSkillsCard;