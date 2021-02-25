
import { Routes, RouterModule } from '@angular/router';
import {NavbarComponent} from './navbar/navbar.component';

const appRoutes: Routes = [
  { path: '', pathMatch: 'full', redirectTo: 'all' }
];

export const routing = RouterModule.forRoot(appRoutes);
