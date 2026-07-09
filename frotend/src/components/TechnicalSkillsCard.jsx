import { Card, CardContent } from "../components/ui/card";
import { Code2 } from "lucide-react";

function TechnicalSkillsCard({ technicalSkills }) {
  return (
    <Card className="rounded-3xl shadow-lg transition-all duration-300 hover:-translate-y-2 hover:scale-[1.02] hover:shadow-2xl">

      <CardContent className="p-8">

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

        <div className="mt-6 flex flex-wrap gap-3">
          {technicalSkills.map((skill, index) => (
            <span
              key={index}
className="rounded-full bg-blue-100 px-4 py-2 text-sm font-semibold text-blue-700 transition-all duration-300 hover:-translate-y-1 hover:scale-105 hover:bg-blue-600 hover:text-white"            >
              {skill}
            </span>
          ))}
        </div>

      </CardContent>

    </Card>
  );
}

export default TechnicalSkillsCard;