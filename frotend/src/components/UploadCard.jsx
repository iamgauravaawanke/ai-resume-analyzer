import { useEffect, useState } from "react";
import { Card, CardContent } from "../components/ui/card";
import { Button } from "../components/ui/button";
import { Upload, FileText } from "lucide-react";
import { analyzedResume, fetchRoles } from "../services/app";

import { useNavigate } from "react-router-dom";


function UploadCard() {
  const [file, setFile] = useState(null);
  const [selectedRoleId, setSelectedRoleId] = useState("");
  const [roles, setRoles] = useState([])


  

  const navigate = useNavigate()


  const handleAnalyse = async() =>{
        if (!file){
            alert("Please Select Pdf: ")
            return;
        }


        if (!selectedRoleId) {
        alert("Please select a role");
        return;
    }

    try{
        const response = await analyzedResume(file, selectedRoleId)          
        console.log(response)



          navigate(`/results/${response.analysis_id}`);
    }
    catch(error){
        console.error("Analysis failed:", error);    }  
    };


  const handleFileChange = (e) => {
    if (e.target.files.length > 0) {
      setFile(e.target.files[0]);
    }
  };


useEffect(() => {
  const loadRoles = async () => {
    try {
      const data = await fetchRoles();

      console.log("Roles:", data);

      setRoles(data.data);
    } catch (error) {
      console.error("Failed to load roles:", error);
    }
  };

  loadRoles();
}, []);

  return (
    <section className="pb-24">
      <div className="container mx-auto flex justify-center px-6">

        <Card className="w-full max-w-2xl rounded-3xl border-0 bg-white shadow-2xl">
          <CardContent className="p-10">

            {/* Title */}
            <div className="text-center">
              <h2 className="text-4xl font-bold text-gray-900">
                Upload Your Resume
              </h2>

              <p className="mt-3 text-gray-500">
                Upload your resume in PDF format and get an AI-powered analysis
                in just a few seconds.
              </p>
            </div>

            {/* Upload Area */}
            <div className="mt-10 rounded-2xl border-2 border-dashed border-blue-300 bg-blue-50 p-10 text-center transition-all duration-300 hover:border-blue-500 hover:bg-blue-100">

              <Upload className="mx-auto h-14 w-14 text-blue-600" />

              <h3 className="mt-5 text-2xl font-semibold text-gray-900">
                Drag & Drop Resume
              </h3>

              <p className="mt-2 text-gray-500">
                or choose a PDF from your computer
              </p>

              <div className="mt-6">
                <input
                  type="file"
                  accept=".pdf"
                  onChange={handleFileChange}
                  className="block w-full cursor-pointer rounded-lg border bg-white p-3 text-sm file:mr-4 file:rounded-md file:border-0 file:bg-blue-600 file:px-4 file:py-2 file:font-medium file:text-white hover:file:bg-blue-700"
                />
              </div>

              {/* File Details */}
              {file && (
                <div className="mt-6 rounded-xl bg-white p-4 text-left shadow-sm">
                  <div className="flex items-center gap-3">
                    <FileText className="h-6 w-6 text-blue-600" />

                    <div>
                      <p className="font-semibold text-gray-900">
                        {file.name}
                      </p>

                      <p className="text-sm text-gray-500">
                        Size: {(file.size / 1024).toFixed(2)} KB
                      </p>

                      <p className="mt-1 text-sm font-medium text-green-600">
                        ✅ Ready for Analysis
                      </p>
                    </div>
                  </div>
                </div>
              )}

              {!file && (
                <div className="mt-5 flex items-center justify-center gap-2 text-sm text-gray-500">
                  <FileText className="h-4 w-4" />
                  PDF only • Maximum 5 MB
                </div>
              )}

            </div>

            <Button
            onClick = {handleAnalyse}
            
              size="lg"
              className="mt-8 w-full rounded-xl bg-blue-600 py-6 text-lg font-semibold hover:bg-blue-700"
            >
              Analyze Resume
            </Button>
        <div className="mt-8">
          <label className="mb-2 block text-left font-semibold text-gray-900">
            Select Target Role
          </label>

          <select
            value={selectedRoleId}
            onChange={(e) => setSelectedRoleId(e.target.value)}
            className="w-full rounded-xl border border-gray-300 bg-white p-3"
          >
            <option value="">Select a role</option>

            {roles.map((role) => (
              <option
                key={role.role_id}
                value={role.role_id}
              >
                {role.role_name}
              </option>
            ))}
          </select>
        </div>
          </CardContent>
        </Card>

      </div>
    </section>
  );
}

export default UploadCard;