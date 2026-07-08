import { Card, CardContent } from "../components/ui/card";
import { Users } from "lucide-react";

function SoftSkillsCard({ softSkills }) {
  return (
    <Card className="rounded-3xl shadow-lg transition-all duration-300 hover:-translate-y-1 hover:shadow-2xl">

      <CardContent className="p-8">

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

        <div className="mt-6 flex flex-wrap gap-3">

          {softSkills.map((skill, index) => (
            <span
              key={index}
              className="rounded-full bg-green-100 px-4 py-2 text-sm font-semibold text-green-700 transition hover:bg-green-600 hover:text-white"
            >
              {skill}
            </span>
          ))}

        </div>

      </CardContent>

    </Card>
  );
}

export default SoftSkillsCard;