import sys
import io
import re
from behave.__main__ import main as behave_main
from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route('/test/scrum_team_retro_view', methods=['GET'])
def run_bdd_tests():
    # Capture the stdout to collect the test results
    stdout_buffer = io.StringIO()
    sys.stdout = stdout_buffer

    # Call the BDD test runner
    behave_main(['--no-capture', '-f', 'pretty'])

    # Restore the original stdout
    sys.stdout = sys.__stdout__

    # Get the captured output
    test_results = stdout_buffer.getvalue()

    # Extract the number of tests passed and failed
    scenarios_passed = r'(\d+) scenarios passed'
    scenarios_failed = r'(\d+) scenarios failed'
    feature_passed = r'(\d+) feature passed'
    feature_failed = r'(\d+) feature failed'
    steps_passed = r'(\d+) steps passed'
    steps_failed = r'(\d+) steps failed'

    sc_passed = re.findall(scenarios_passed, test_results)
    sc_failed = re.findall(scenarios_failed, test_results)
    fe_passed = re.findall(feature_passed, test_results)
    fe_failed = re.findall(feature_failed, test_results)
    st_passed = re.findall(steps_passed, test_results)
    st_failed = re.findall(steps_failed, test_results)

    # Construct the response
    response = {
        'scenarios passed': int(sc_passed[0]) if sc_passed else 0,
        'scenarios failed': int(sc_failed[0]) if sc_failed else 0,
        'feature passed': int(fe_passed[0]) if fe_passed else 0,
        'feature failed': int(fe_failed[0]) if fe_failed else 0,
        'steps passed': int(st_passed[0]) if st_passed else 0,
        'steps failed': int(st_failed[0]) if st_failed else 0
    }


    # Return the test results as a JSON response
    return render_template('test_result.html', response=response)

# Other routes and API logic

if __name__ == '__main__':
    app.run()
