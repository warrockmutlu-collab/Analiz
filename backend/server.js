const express = require('express');
const axios = require('axios');
const cors = require('cors');
require('dotenv').config();

const app = express();
const PORT = process.env.PORT || 5000;

app.use(cors());
app.use(express.json());

const API_KEY = process.env.API_FOOTBALL_KEY;
const API_BASE_URL = 'https://api-football-v1.p.rapidapi.com/v3';

app.get('/api/matches', async (req, res) => {
    try {
        const { league, season } = req.query;
        const response = await axios.get(`${API_BASE_URL}/fixtures`, {
            headers: {
                'x-rapidapi-key': API_KEY,
                'x-rapidapi-host': 'api-football-v1.p.rapidapi.com'
            },
            params: {
                league: league || 39,
                season: season || 2024
            }
        });
        res.json(response.data);
    } catch (error) {
        console.error('Error fetching matches:', error);
        res.status(500).json({ error: 'Failed to fetch matches' });
    }
});

app.get('/api/match/:id/stats', async (req, res) => {
    try {
        const { id } = req.params;
        const response = await axios.get(`${API_BASE_URL}/fixtures`, {
            headers: {
                'x-rapidapi-key': API_KEY,
                'x-rapidapi-host': 'api-football-v1.p.rapidapi.com'
            },
            params: {
                id: id
            }
        });
        res.json(response.data);
    } catch (error) {
        console.error('Error fetching match stats:', error);
        res.status(500).json({ error: 'Failed to fetch match stats' });
    }
});

app.get('/api/health', (req, res) => {
    res.json({ status: 'Server is running' });
});

app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});