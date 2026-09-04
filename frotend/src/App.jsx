
import Home from "./pages/Home";
import Results from "./pages/Result";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import  LearningResources from "./pages/LearningResources"
import  InterviewPreparation  from "./pages/InterviewPreparation"
import InterviewQuestion from "./pages/InterviewQuestion"
import LearningProgress from "./pages/LearningProgress";
import CareerCoach from "./pages/CareerCoach";

function App() {
  return (
<BrowserRouter>



<Routes>

  <Route
    path=""
    element={<Home />}
  />

  <Route
    path="/results/:analysis_id"
    element={<Results />}
  />

  <Route
    path="/result/:analysis_id"
    element={<Results />}
  />

  <Route
    path="/learning-resources/:analysis_id"
    element={<LearningResources />}
  />

  <Route
    path="/interview-preparation/:role_id"
    element={<InterviewPreparation />}
  />

  <Route
    path="/learning-progress/:resume_id"
    element={<LearningProgress />}
  />

  <Route
    path="/interview-preparation/:role_id/question/:question_id"
    element={<InterviewQuestion />}
  />


 <Route
  path="/carrer-chat/:resume_id"
  element= {<CareerCoach/>}
 />

</Routes>



</BrowserRouter>
  );
}

export default App;