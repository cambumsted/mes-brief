# Marketing Effectiveness Solution — Brief

A static, self-contained pitch document for the Marketing Effectiveness Solution.

## Files
- `index.html` — the brief itself (open in any browser to view)
- `staticwebapp.config.json` — Azure Static Web Apps config (locks the site behind Microsoft AAD sign-in)

## Local preview
Just double-click `index.html`, or open it in any browser. No build step.

---

## Deploying to Azure Static Web Apps (Microsoft-only access)

This gives you a real shareable URL that requires Microsoft AAD sign-in.

### 1. Push this folder to a GitHub repo
Create a private repo (e.g., `mes-brief`) and push these files to the `main` branch.

### 2. Create the Static Web App in the Azure Portal
1. Go to **portal.azure.com** → **Create a resource** → search **Static Web App**
2. Fill in:
   - **Subscription:** your team / personal Azure subscription
   - **Resource Group:** create new (e.g., `rg-mes-brief`)
   - **Name:** `mes-brief`
   - **Plan type:** Free
   - **Region:** nearest to you (e.g., West US 2)
   - **Source:** GitHub → authorize → pick the repo and `main` branch
   - **Build presets:** Custom
     - App location: `/`
     - Output location: *(leave blank)*
3. **Review + Create**.

Azure will commit a GitHub Actions workflow to your repo and run the first deploy in ~2 minutes.

### 3. Test
- Once deployment finishes, open the URL Azure assigns (something like `https://thankful-meadow-12345.westus2.azurestaticapps.net`).
- You'll be redirected to Microsoft sign-in.
- After sign-in with your @microsoft.com account, the page loads.

### 4. Share
- Copy the URL and send it to your reviewers.
- Anyone with a Microsoft tenant account who has the link can view (the `staticwebapp.config.json` allows any authenticated AAD user — see "Restricting further" below if you want a tighter ACL).

### 5. Iterate
- Edit `index.html` locally, commit, push to `main`. Site auto-redeploys in ~1 minute.

---

## Restricting further (optional)

The current config allows **any signed-in Microsoft tenant user**. To restrict to specific people:

1. In the Azure Portal, open your Static Web App → **Role management**
2. Invite specific email addresses and assign a custom role (e.g., `mes-reviewer`)
3. Update the `allowedRoles` in `staticwebapp.config.json`:
   ```json
   "allowedRoles": ["mes-reviewer"]
   ```
4. Commit + push to redeploy.

---

## About the AAD config

The `openIdIssuer` in `staticwebapp.config.json` uses the Microsoft tenant ID (`72f988bf-86f1-41af-91ab-2d7cd011db47`), which restricts sign-in to Microsoft AAD accounts only.

If you're not in the Microsoft tenant, replace that GUID with your own tenant ID (Azure Portal → Microsoft Entra ID → Overview → Tenant ID).

---

## Cost
Free tier covers this use case (low traffic, static content). No credit card charges expected.

## If you can't use Azure
Easier alternatives:
- **SharePoint Page** on your team site (built-in comments, native Microsoft auth)
- **Email the `index.html` as an attachment** — recipients open locally in their browser
