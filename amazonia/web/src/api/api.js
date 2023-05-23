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
    baseURL: 'https://amazonia-xi.vercel.app/',
  },
  (config.CancelToken = CancelToken)
);

export default api;
