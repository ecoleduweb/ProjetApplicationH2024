// import { test, expect } from '@playwright/test';

// test.beforeEach(async ({ page }) => {
//     // se connecte au site (ADDRESSE A CHANGER LORSQUE LE SITE SERA DÉPLOYÉ)
//     await page.goto('http://localhost:5173/offre');
//     await 1000;
//     await page.waitForLoadState('networkidle');
//   });


//   test('Ajouter un Offre', async ({ page }) => {
//   await page.getByLabel('Titre du poste*').click();
//   await page.getByLabel('Titre du poste*').fill('Deuxieme Tech');
//   await page.getByPlaceholder('Choisir période(s)').click();
//   await page.getByRole('option', { name: 'Temps plein' }).click();
//   await page.getByText('Créer une nouvelle offre d\'emploi Titre du poste* Type d\'emplois* Temps plein').click();
//   await page.getByLabel('Salaire (Heure)*').click();
//   await page.getByLabel('Salaire (Heure)*').fill('Riviere-du-Loup'); 
//   await page.getByLabel('Date d\'entrée en fonction*').fill('2024-03-11');
//   await page.getByLabel('Date limite pour postuler*').fill('2024-03-11');
//   await page.getByPlaceholder('Choisir programme(s)').click();
//   await page.getByRole('option', { name: 'Informatique' }).click();

//   await page.getByLabel('Heure (Semaine)*').click();
//   await page.locator('form div').filter({ hasText: 'Salaire (Heure)*' }).locator('#salaire').click();
//   await page.locator('form div').filter({ hasText: 'Salaire (Heure)*' }).locator('#salaire').fill('15');
//   await page.getByLabel('Heure (Semaine)*').click();
//   await page.getByLabel('Heure (Semaine)*').fill('35');
//   await page.getByLabel('Urgente').check();
//   await page.getByLabel('Lien*').click();
//   await page.getByLabel('Lien*').fill('patate123.ca');
//   await page.getByLabel('Courriel contact*').click();
//   await page.getByLabel('Courriel contact*').fill('Gilles Dubé');
//   await page.getByLabel('Description du poste*').click();
//   await page.getByLabel('Description du poste*').fill('Lorem Ipsum');
//   await page.getByRole('button', { name: 'Enregistrer' }).click();
// });