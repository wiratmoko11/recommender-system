import math
# Matrix Initialization
n, m = 100, 100;
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
m=5; # banyak user (baris)
n=6; # banyak item (kolom)
Matrix = [[0 for x in range(n)] for y in range(m)]
Mean_P = [[0 for x in range(n)] for y in range(m)]


# Data
Matrix[0][0] =  7.0;  Matrix[0][1] =  6.0; Matrix[0][2] =  7.0; Matrix[0][3] =  4.0; Matrix[0][4] =  5.0; Matrix[0][5] =  4.0; 
Matrix[1][0] =  6.0;  Matrix[1][1] =  7.0; Matrix[1][2] =  '?'; Matrix[1][3] =  4.0; Matrix[1][4] =  3.0; Matrix[1][5] =  4.0;
Matrix[2][0] =  '?';  Matrix[2][1] =  3.0; Matrix[2][2] =  3.0; Matrix[2][3] =  1.0; Matrix[2][4] =  1.0; Matrix[2][5] =  '?';
Matrix[3][0] =  1.0;  Matrix[3][1] =  2.0; Matrix[3][2] =  2.0; Matrix[3][3] =  3.0; Matrix[3][4] =  3.0; Matrix[3][5] =  4.0;
Matrix[4][0] =  1.0;  Matrix[4][1] =  '?'; Matrix[4][2] =  1.0; Matrix[4][3] =  2.0; Matrix[4][4] =  3.0; Matrix[4][5] =  3.0;


def selectSort(alist):
   for fillslot in range(len(alist)-1,0,-1):
      positionOfMax=0
      for location in range(1,fillslot+1):
         if alist[location]<alist[positionOfMax]:
            positionOfMax = location

      alist[fillslot], alist[positionOfMax] = alist[positionOfMax], alist[fillslot]


def matrix(row, col, value):
   Matrix[row-1][col-1] = value


def data():
   print("Data table")
   # Show data table
   for i in range(n+1):
      if(i == 0):
         print('   ', end='')
      else:
         print('  ', i, '  ', end='')
   print("")
            
   for i in range (m):
      print('', alphabet[i], '', end='')
      for j in range (n):
         value = Matrix[i][j]
         a = str(value)
         if(len(a)>1):
            print('[ ' + a + ' ]', end='')
         else:
            print('[  ?  ]', end='')
      print("")
      
   print("")


# Main program algorithm
def sim(user):
   pearson=[]
   s_pearson=[]
   mean=[]
   top_k=[]
   for i in range(n+1):
      if(i == 0):
         print('   ', end='')
      else:
         print('  ', i, '  ', end='')
   print("   Mean     Pearson( i ,", user, ")")
   
   # Calculating mean
   for i in range (m):
      M=0; count=0
      for j in range (n):
         if Matrix[i][j] != '?':
            M = M + Matrix[i][j]
            count = count+1

      mean.append(round(M/count, 1))
      for j in range (n):
         if Matrix[i][j] != '?':
            Mean_P[i][j] = round(Matrix[i][j]-mean[i], 2)
         else:
            Mean_P[i][j] = '?'

   # Pearson corelation
   for i in range (m):
      top=0; a=0; b=0;
      for j in range (n):
         if Mean_P[user-1][j] != '?' and Mean_P[i][j] != '?' :
            top = round(top + Mean_P[i][j]*Mean_P[user-1][j], 3)
            a = round(a + math.pow(Mean_P[i][j],2), 3)
            b = round(b + math.pow(Mean_P[user-1][j],2), 3)
      
      pearson.append(round (top / ((math.pow(a, 0.5))*(math.pow(b, 0.5))), 3))
      s_pearson.append(round (top / ((math.pow(a, 0.5))*(math.pow(b, 0.5))), 3))
      
      print('', alphabet[i], '', end='')
      for j in range (n):
         value = Matrix[i][j]
         data = str(value)
         if(len(data)>1):
            print('[ ' + data + ' ]', end='')
         else:
            print('[  ?  ]', end='')

      print(' [ ', mean[i], end='  ]')
      print('      ', pearson[i])

   # Rating prediction
   selectSort(s_pearson)
   k = int(input("\nTop k = "))
   print("User:", user)
   s_pearson.pop(0)
   while(len(s_pearson)>k):
      s_pearson.pop()

   
   for h in range (n):
      top=0; bot=0;
      if Matrix[user-1][h] == '?':
         for i in range (len(s_pearson)):
            for j in range (len(pearson)):
               if s_pearson[i] == pearson[j]:
                  top = round(top + Matrix[j][h]*pearson[j], 3)
                  bot = round(bot + pearson[j], 3)

         print("\nRating prediction for item", h+1, "=", top/bot)
         Matrix[user-1][h] = round(top/bot, 1)

