# GitHub Actions Acceptance Tests

This workflow runs acceptance tests across multiple hosts and publishes results to GitHub Pages.

## Setup

### 1. Enable GitHub Pages

1. Go to your repository Settings → Pages
2. Set **Source** to: `Deploy from a branch`
3. Set **Branch** to: `gh-pages` and `/ (root)`
4. Click Save

### 2. Run the Workflow

The workflow can be triggered manually:

1. Go to **Actions** tab in your repository
2. Select **Run Acceptance Tests** workflow
3. Click **Run workflow**
4. (Optional) Customize the hosts to test

## Features

- **Multi-host Testing**: Tests run in parallel on `volt`, `ampere`, and `tesla`
- **History Retention**: Keeps last 20 test runs with trends
- **GitHub Pages**: Automatic deployment to `https://<username>.github.io/<repo>/`
- **Environment Labels**: Results are tagged by host in Allure report

## Workflow Jobs

### 1. `test`
Runs pytest on each host in parallel:
- Sets `TEST_HOST` environment variable
- Collects Allure results per host
- Uploads results as artifacts

### 2. `publish-report`
Combines results and publishes to GitHub Pages:
- Downloads all host results
- Merges into single Allure report
- Retrieves history from `gh-pages` branch
- Generates report with trends
- Deploys to GitHub Pages

## Local Testing

To simulate a specific host locally:

```bash
# Set host environment variable
export TEST_HOST=volt

# Run tests
pytest

# View report
allure-serve
```

## Viewing Results

After workflow completion, reports are available at:
```
https://<username>.github.io/<repo>/
```

The report includes:
- Test results grouped by suite (Operations, Performance, Security, Reliability)
- Host-specific filtering
- Historical trends (last 20 runs)
- Detailed test steps and logs
