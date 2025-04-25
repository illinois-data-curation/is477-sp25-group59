# Status Report

## Progress Update

### Week 8-9: Reproducible Package Setup

**Tasks Completed:**

- **Python Package Structure**: 
  Over the past couple of weeks, I’ve been busy setting up the Python package structure. This involved creating directories for the source code (`src/`), documentation (`docs/`), and tests (`tests/`). This setup ensures that everything is organized and easy to navigate. 

- **CLI Script Development**: 
  One of the major tasks was developing the CLI script (`pipeline.py`). This script is the backbone of the project, handling the entire data pipeline from downloading and cleaning the data to merging and analyzing it. It’s designed to be user-friendly, so you can run different parts of the pipeline with simple commands.

- **README.md**: 
  I also wrote a README.md file. This document is crucial as it provides clear installation and setup instructions for anyone who wants to use the package. It’s like the instruction manual that comes with a new gadget, making sure you know how to get started and make the most of it. This file will be updated as more progress is made.

- **Unit Tests**: 
  To ensure everything works smoothly, I did unit tests for the core functions. These tests are essential for verifying that the code behaves as expected and helps catch any bugs early on. 

**Artifacts**:
- Python Package Structure
- CLI Script
- README.md
- Unit Tests

### Week 10-11: Workflow Automation

**Current Status**:

- **Makefile and CLI Wrapper**: 
  I’ve just started working on the Makefile and CLI wrapper. These tools will automate the steps of the data pipeline, making it easier to run the entire process with a single command. 

- **Logging and Error Handling**: 
  Initial setup for logging and error handling has just started being implemented in the CLI script. This ensures that any issues are logged, and you get clear messages about what went wrong. I wanted to have a troubleshooting guide that helps you fix problems quickly.

- **Testing Automation**: 
  Testing the automation in a clean environment is planned for the upcoming week. This step is crucial to ensure that the pipeline works seamlessly from start to finish. 

- **Refactoring Scripts**: 
  Refactoring scripts based on test results will be done after initial testing. This involves cleaning up the code, improving its efficiency, and making sure it’s easy to understand.

**Artifacts**:
- Pipeline Script with Logging

### Delay and Changes to Project Plan

**Reason for Delay**:

- The initial dataset I chose didn’t contain the sponsorship data I needed for my original research question. This was a bit of a setback because I had to spend a few days searching for related datasets that could help answer the question. Unfortunately, I couldn’t find any suitable datasets, which meant I had to rethink my approach.

**Changes to Research Question**:

- After some consideration, I decided to change the research question to focus on the evolution of lap times across different circuits. This new direction is still exciting and relevant, and it aligns well with the data I have. It did mean redoing some of the tasks done on Week 8-9, but I’m confident this new focus will yield interesting insights.

**Updated Tasks**:

- **Data Acquisition**: 
  I’m now focusing on lap times and race circuit data from the Kaggle dataset. This involves downloading the relevant data and making sure it’s ready for analysis.

- **Data Cleaning**: 
  The cleaning process has been adjusted to handle lap times and race circuit data. This involves removing any missing values and ensuring the data is consistent and accurate.

- **Data Merging**: 
  I’ve updated the merging process to combine lap times data with race circuit information. This step is crucial for creating a comprehensive dataset that can be analyzed.

- **Data Analysis**: 
  The analysis will now focus on the evolution of lap times across different circuits over the years. This involves calculating mean lap times for each circuit and year and looking for trends and patterns.

## Updated Timeline

### Week 10-11: Workflow Automation
- **Makefile and CLI Wrapper**
- **Logging and Error Handling**
- **Testing Automation**
- **Refactoring Scripts**

### Week 12: Metadata & Citations
- **CITATION.md**
- **Licensing Files**
- **Dataset Metadata**

### Week 13-15: Final Archiving
- **GitHub-Zenodo Integration**
- **DOI and Citation Info**

## Next Steps

1. **Complete Workflow Automation**: 
   The next big task is to finish developing the Makefile and CLI wrapper. This will involve adding robust logging and error handling and testing the automation in a clean environment. It’s a critical step to ensure the pipeline runs smoothly and efficiently.

2. **Metadata & Citations**: 
   Once the automation is in place, I’ll focus on creating CITATION.md, adding licensing files, and drafting dataset metadata. This will ensure clear citations and data provenance, which are essential for the project’s credibility and reproducibility.

3. **Final Archiving**: 
   The final step will be to integrate the project with GitHub-Zenodo for long-term archiving. This will involve adding DOI and citation information to the documentation, ensuring the project is well-documented and shareable.

## Conclusion

Despite the initial delay due to dataset issues, the project is now back on track with a revised research question and updated tasks. The reproducible package setup has been completed, and workflow automation is currently in progress. The next steps will focus on metadata, citations, and final archiving to ensure the project is well-documented and shareable.

I’m excited about the new direction of the project and looking forward to uncovering interesting insights about the evolution of lap times in Formula 1. It’s been a challenging but rewarding journey so far, and I’m confident that the final product will be both informative and valuable.