
import Home from "./pages/Home";
import Results from "./pages/Result";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import  LearningResources from "./pages/LearningResources"
import  InterviewPreparation  from "./pages/InterviewPreparation"
import InterviewQuestion from "./pages/InterviewQuestion"
import LearningProgress from "./pages/LearningProgress";

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

</Routes>



</BrowserRouter>
  );
}

export default App;