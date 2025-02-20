import axios from "axios";

let refresh = false;

axios.interceptors.response.use(
  (resp) => resp,
  async (error) => {
    if (error.response.status === 401 && !refresh) {
      refresh = true;
      console.log(localStorage.getItem('refresh_token'));

      try {
        const response = await axios.post(
          'https://facesecure.azurewebsites.net/token/refresh/',
          {
            refresh: localStorage.getItem('refresh_token'),
          },
          {
            headers: {
              'Content-Type': 'application/json',
            },
            withCredentials: false,
          }
        );

        if (response.status === 200) {
          axios.defaults.headers.common['Authorization'] = `Bearer ${response.data['access']}`;
          localStorage.setItem('access_token', response.data.access);
          localStorage.setItem('refresh_token', response.data.refresh);
          return axios(error.config);
        }
      } catch (refreshError) {
        console.error('Error refreshing token:', refreshError);
      }
    }

    refresh = false;
    return Promise.reject(error);
  }
);

export default axios;
