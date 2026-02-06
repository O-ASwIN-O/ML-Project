from flask import Flask,request,render_template
import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData,PredictPipeline

application=Flask(__name__)

app=application

## Route for a home page

@app.route('/')
def index():
    try:
        return render_template('index.html')
    except Exception as e:
        import traceback
        error_msg = f"Error in index route: {str(e)}\n{traceback.format_exc()}"
        print(error_msg)
        return f"<h1>Error</h1><pre>{error_msg}</pre>", 500 

@app.route('/predictdata',methods=['GET','POST'])
def predict_datapoint():
    if request.method=='GET':
        try:
            return render_template('home.html')
        except Exception as e:
            import traceback
            error_msg = f"Error rendering home.html: {str(e)}\n{traceback.format_exc()}"
            print(error_msg)
            return f"<h1>Template Error</h1><pre>{error_msg}</pre>", 500
    else:
        try:
            data=CustomData(
                gender=request.form.get('gender'),
                race_ethnicity=request.form.get('ethnicity'),
                parental_level_of_education=request.form.get('parental_level_of_education'),
                lunch=request.form.get('lunch'),
                test_preparation_course=request.form.get('test_preparation_course'),
                reading_score=float(request.form.get('reading_score')),
                writing_score=float(request.form.get('writing_score'))
            )
            pred_df=data.get_data_as_data_frame()
            print(pred_df)
            print("Before Prediction")

            predict_pipeline=PredictPipeline()
            print("Mid Prediction")
            results=predict_pipeline.predict(pred_df)
            print("after Prediction")
            return render_template('home.html',results=results[0])
        except Exception as e:
            import traceback
            import os
            
            cwd = os.getcwd()
            files_in_cwd = os.listdir(cwd)
            artifacts_content = "artifacts folder not found"
            if os.path.exists("artifacts"):
                artifacts_content = str(os.listdir("artifacts"))
            
            error_msg = f"""Error during prediction: {str(e)}
            
            --- Debug Info ---
            CWD: {cwd}
            Files in CWD: {files_in_cwd}
            Artifacts content: {artifacts_content}
            Traceback:
            {traceback.format_exc()}"""
            
            print(error_msg)
            return f"<h1>Prediction Error</h1><pre>{error_msg}</pre>", 500
    

if __name__=="__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)        


