
import Home from "./pages/Home";
import Results from "./pages/Result";
import { BrowserRouter, Routes, Route } from "react-router-dom";

function App() {
  return (
<BrowserRouter>

<Routes>



<Route
path=""
element={<Home/>}  />


<Route
    path="/results/:analysis_id"
element={<Results/>} />



<Route
    path="/result/:analysis_id"
    element={<Results />}
/>
</Routes>


</BrowserRouter>
  );
}

export default App;