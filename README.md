# unofficial NPBAPI
unofficial NPBAPIは、日本プロ野球の試合速報・試合結果をJSON形式で提供する非公式のAPIです。  
_unofficial NPBAPI is an unofficial API that provides live scores and match results of Japanese professional baseball in JSON format._  
## how to use 
### 試合速報 *live scores*    
request  
`GET https://npbapi-147514.appspot.com/score/today/`  
response 
    
    {  
      "game": [  
        {  
          "inning": "after",   
          "home_team": "T",   
          "home_score": "3", 
          "visitor_team": "G", 
          "visitor_score": "0", 
          "start_at": "14:00"
        }, 
        {
          "inning": "5b", 
          "home_team": "C", 
          "home_score": "3", 
          "visitor_team": "S", 
          "visitor_score": "1", 
          "start_at": "18:00"
        }, 
        {
          "inning": "4t", 
          "home_team": "E", 
          "home_score": "8", 
          "visitor_team": "Bs", 
          "visitor_score": "1", 
          "start_at": "18:00"
        }
      ]
    }  
### 試合結果 *match results*  
request  
`GET https://npbapi-147514.appspot.com/score/yyyymmdd/`  
response  

    {
      "game": [
        {
          "date": "20160929", 
          "home_team": "G", 
          "home_score": "3", 
          "visitor_team": "C", 
          "visitor_score": "5", 
          "start_at": "18:00"
        }, 
        {
          "date": "20160929", 
          "home_team": "DB", 
          "home_score": "6", 
          "visitor_team": "S", 
          "visitor_score": "11", 
          "start_at": "18:00"
        }, 
        {
          "date": "20160929", 
          "home_team": "Bs", 
          "home_score": "2", 
          "visitor_team": "E", 
          "visitor_score": "10", 
          "start_at": "18:00"
        }
      ]
    }
