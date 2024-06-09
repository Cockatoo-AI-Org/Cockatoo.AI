// src/App.js 
// Author: Louis Chang
// DESCRIPTION: This file contains the main App component for the React application.
// Version 0.2 - 2024/06/09

// - Version 0.1 - 2024/06/02: Create the main App component.
// - Version 0.2 - 2024/06/09: Add routes for Chat and Settings components.

import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Chat from './Chat';
import Settings from './Settings';
import Navbar from './Navbar';

function App() {
    return (
        <Router>
            <div className="App">
                <Navbar />
                <div className="container">
                    <Routes>
                        <Route path="/" element={<Chat />} />
                        <Route path="/settings" element={<Settings />} />
                    </Routes>
                </div>
            </div>
        </Router>
    );
}

export default App;
