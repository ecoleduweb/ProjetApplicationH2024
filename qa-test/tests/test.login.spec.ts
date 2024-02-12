import { test, expect } from '@playwright/test';
import { time } from 'console';


test.beforeEach(async ({ page }) => {
  // se connecte au site (ADDRESSE A CHANGER LORSQUE LE SITE SERA DÉPLOYÉ)
  await page.goto('http://localhost:5173/');
  await 1000;
  await page.waitForLoadState('networkidle');
});


test('Site Available', async ({ page }) => {
  const text = await page.textContent('body'); // va chercher le texte complet de la page actuel
  expect(text).toContain('test@cegeprdl.ca'); // recherche le texte
});

test('Register', async ({ page }) => {
  // Ouvre la page de connexion
  await page.getByRole('link', { name: 'Se connecter' }).click();
  // Ouvre la page de création d'utilisateur
  await page.getByRole('link', { name: 'Créer un utilisateur' }).click();
  // Rempli les champs
  await page.getByLabel('Prénom').click();
  await page.getByLabel('Prénom').fill('test');
  await page.getByLabel('Prénom').press('Tab');
  await page.getByLabel('Nom de famille').fill('test');
  await page.getByLabel('Nom de famille').press('Tab');
  await page.getByLabel('Nom Entreprise').fill('Test Rdl');
  await page.getByLabel('Nom Entreprise').press('Tab');
  await page.getByLabel('Adresse').fill('Route du Test');
  await page.getByLabel('Adresse').press('Tab');
  await page.getByLabel('Ville').fill('Riviere-du-Loup');
  await page.getByLabel('Ville').press('Tab');
  await page.getByLabel('Code Postal').fill('G5R1R1');  
  await page.getByLabel('Code Postal').press('Tab');
  await page.getByLabel('Province').click();
  await page.getByLabel('Province').fill('Quebec');
  await page.getByLabel('Province').press('Tab');
  await page.getByLabel('Courriel').fill('test');
  await page.getByLabel('Courriel').press('Alt+Control+2');
  await page.getByLabel('Courriel').fill('test@test.ca');
  await page.getByLabel('Mot de passe').click();
  await page.getByLabel('Mot de passe').fill('Patate123');
  await page.locator('#confirm_password').click();
  await page.locator('#confirm_password').fill('Patate123');
  //confirme la création du compte
  await page.getByRole('button', { name: 'Créer' }).click();
  // MANQUE LA VALIDATION AVEC API... A faire
});

test('Login', async ({ page }) => {
  await page.getByRole('link', { name: 'Se connecter' }).click();
  await page.getByLabel('Nom d\'utiliasteur').click();
  await page.getByLabel('Nom d\'utiliasteur').fill('test@test.ca');
  await page.getByLabel('Nom d\'utiliasteur').press('Tab');
  await page.getByLabel('Mot de passe').fill('Patate123');
  await page.getByLabel('Mot de passe').press('Control+a');
  await page.getByLabel('Mot de passe').fill('Patate123');
  await page.getByRole('button', { name: 'Se connecter' }).click();
  // MANQUE LA VALIDATION AVEC API... A faire
});

test('Forgot Password', async ({ page }) => {
  await page.getByRole('link', { name: 'Se connecter' }).click();
  await page.getByRole('link', { name: 'Mot de passe oublié ?' }).click();
  await page.getByLabel('Entrez votre courriel').click();
  await page.getByLabel('Entrez votre courriel').fill('test@test.ca');
  await page.getByRole('button', { name: 'Confirmer' }).click();
  // MANQUE LA VALIDATION AVEC API... A faire
});