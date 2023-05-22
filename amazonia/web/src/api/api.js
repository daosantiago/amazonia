import axios from 'axios';
const CancelToken = axios.CancelToken;

const config = {
  headers: {
    'Content-Type': 'application/json',
    'Cache-Control': 'no-cache, no-store, must-revalidate',
    Pragma: 'no-cache',
    Expires: '0',
  },
};

const api = axios.create(
  {
    baseURL: 'http://127.0.0.1:8000/',
  },
  (config.CancelToken = CancelToken)
);

export default api;
