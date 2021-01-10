import Main from './components/Main/Main'
import Login from './components/User/Login'
import Register from './components/User/Register'
import Services from './components/Main/Services'
import Profile from './components/User/Profile'
import Booking from './components/User/Booking'
import AddHotel from './components/Admin/AddHotel'
import Requests from './components/Admin/Requests'
import Statistics from './components/Admin/Statistics'
import AddService from './components/Admin/AddService'
import AddManager from './components/Admin/AddManager'
import CheckIn from './components/Manager/CheckIn'
import CheckOut from './components/Manager/CheckOut'
import Schedule from './components/Manager/Schedule'
import Housekeeping from './components/Manager/Housekeeping'


export default [
    { path: '/', component: Main },
    { path: '/login', component: Login },
    { path: '/register', component: Register },
    { path: '/services', component: Services },
    { path: '/profile', component: Profile },
    { path: '/booking', component: Booking },
    { path: '/admin/add-hotel', component: AddHotel },
    { path: '/admin/requests', component: Requests },
    { path: '/admin/statistics', component: Statistics },
    { path: '/admin/add-service', component: AddService },
    { path: '/admin/add-manager', component: AddManager },
    { path: '/manager/check-in', component: CheckIn },
    { path: '/manager/check-out', component: CheckOut },
    { path: '/manager/schedule', component: Schedule },
    { path: '/manager/housekeeping', component: Housekeeping },

]