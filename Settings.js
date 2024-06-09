// src/Settings.js 
// Author: Louis Chang
// DESCRIPTION: This file contains the implementation of a settings component for configuring the LLM.
// Version 0.2 - 2024/06/09

// - Version 0.1 - 2024/06/02: Create the settings component.
// - Version 0.2 - 2024/06/09: Add the functionality to change model settings.

import React, { useState } from 'react';

function Settings() {
    const [maxTokens, setMaxTokens] = useState(2056);
    const [doSample, setDoSample] = useState(true);
    const [temperature, setTemperature] = useState(0.9);
    const [model, setModel] = useState('google/gemma-7b-it');

    const handleSubmit = async (e) => {
        e.preventDefault();
        const response = await fetch('http://localhost:8000/settings', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                max_new_tokens: maxTokens,
                do_sample: doSample,
                temperature: temperature,
                model: model,
            }),
        });
        if (response.ok) {
            alert('Settings updated successfully!');
        } else {
            alert('Failed to update settings.');
        }
    };

    return (
        <div className="mt-5">
            <h2>Settings</h2>
            <form onSubmit={handleSubmit}>
                <div className="form-group">
                    <label>Max New Tokens</label>
                    <input 
                        type="number" 
                        className="form-control" 
                        value={maxTokens} 
                        onChange={(e) => setMaxTokens(e.target.value)} 
                    />
                </div>
                <div className="form-group">
                    <label>Do Sample</label>
                    <select 
                        className="form-control" 
                        value={doSample} 
                        onChange={(e) => setDoSample(e.target.value === 'true')} 
                    >
                        <option value="true">True</option>
                        <option value="false">False</option>
                    </select>
                </div>
                <div className="form-group">
                    <label>Temperature</label>
                    <input 
                        type="number" 
                        step="0.1" 
                        className="form-control" 
                        value={temperature} 
                        onChange={(e) => setTemperature(e.target.value)} 
                    />
                </div>
                <div className="form-group">
                    <label>Model</label>
                    <select 
                        className="form-control" 
                        value={model} 
                        onChange={(e) => setModel(e.target.value)} 
                    >
                        <option value="google/gemma-7b-it">Google Gemma 7B</option>
                        <option value="other/model-1">Other Model 1</option>
                        <option value="other/model-2">Other Model 2</option>
                    </select>
                </div>
                <button type="submit" className="btn btn-primary mt-3">Save</button>
            </form>
        </div>
    );
}

export default Settings;
