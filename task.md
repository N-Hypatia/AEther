# Task Analysis - AEther Project Setup

## Current State Analysis

### Project Type
Scientific visualization tool for Minkowski spacetime physics

### Existing Components
1. **Minkowski's Space-Time Visualizer** - Basic event visualization
2. **light-cone-plot** - 2D/3D light cone plotting
3. **3d-light-cone-plot** - Alternative 3D visualization
4. **src/lorentz.py** - Lorentz transformation module (301 chars)

### Gap Analysis
- No test structure
- No CI/CD pipeline
- No security scanning (bandit)
- No coverage tracking
- Missing README badges
- No pre-commit hooks

## Required Tasks (Rule 26)

### Infrastructure Tasks (5 items)
1. **Setup pytest + pytest-cov** - Test infrastructure with 60% minimum coverage target
2. **Configure pre-commit with bandit** - Security scanning on every commit
3. **Create GitHub Actions workflow** - CI/CD for testing and security
4. **Add requirements.txt** - Python dependencies management
5. **Create demo scripts** - Working examples for validation

### Priority
- Task 1: Tests first (Rule 5 - 60% coverage mandatory)
- Task 2: Security scanning (Rule 6 - bandit mandatory)
- Task 3: CI/CD pipeline
- Task 4: Dependencies
- Task 5: Demos (2 required per milestone - Rule 18)

## Progress Tracking

| Milestone | Target | Current |
|-----------|--------|---------|
| Initial Setup | 5% | 5% |
| Test Infrastructure | 10% | 0% |
| Security Config | 15% | 0% |
| CI/CD | 20% | 0% |
| Working Demos | 25% | 0% |

## Blockers
- None identified

## Next Actions
1. Create tests/ directory with initial test files
2. Add pytest configuration (pytest.ini or pyproject.toml)
3. Add safety check to requirements