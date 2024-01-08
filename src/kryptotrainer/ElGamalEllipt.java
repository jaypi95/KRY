package kryptotrainer;

import mybiginteger.*;


public class ElGamalEllipt {
	
	
	  BigInteger p;   //Primzahl für GF(p)
	  
	  BigInteger a,b;  //Parameter für die elliptische Kurve (y^2 = x^3 + ax + b)
	  
	  BigInteger[] P = {BigInteger.ZERO, BigInteger.ZERO};  //ausgewählter Punkt (x,y) der elliptischen Kurve
	  
	  BigInteger kA, kB; //geheimer Schlüssel von Alice resp. von Bob
	  
	  BigInteger[] A =  {BigInteger.ZERO, BigInteger.ZERO};  //oeffentlicher Schluessel von Alice 
	  

	  /************************************************************************
	   ************************************************************************
	   * Methoden, die ausprogrammiert werden müssen.
	   ************************************************************************
	   ************************************************************************/
	  
	  
	    /**
	     * Berechnet die Verschlüsselung fuer eine Nachricht M, die als Punkt auf der elliptischen Kurve gegeben ist.
	     * @throws Exception 
	     */
	    
	    public BigInteger[] elliptEncrypt(BigInteger[] M) throws Exception 
	    {
			    BigInteger[] B = {BigInteger.ZERO, BigInteger.ZERO};
				BigInteger[] C = {BigInteger.ZERO, BigInteger.ZERO};
				B = P[0].elliptMultiply(P[1], kB, p, a, b);
				BigInteger temp[] = A[0].elliptMultiply(A[1], kB, p, a, b);
				C = temp[0].elliptAdd(temp[1], M[0], M[1], p, a, b);
				BigInteger result[] = {B[0], B[1], C[0], C[1]};
				return result;
	    }
	    
	    
	    /**
	     * Berechnet die Entschlüsselung für die Nachricht (B,C) mithilfe von k_A.
	     * @throws Exception 
	     */
	    
	    public BigInteger[] elliptDecrypt(BigInteger[] B, BigInteger[] C) throws Exception 
	    
	    {
			BigInteger[] result = {BigInteger.ZERO, BigInteger.ZERO};
			BigInteger temp[] = B[0].elliptMultiply(B[1].negate().add(p), kA, p, a, b);
			result = temp[0].elliptAdd(temp[1], C[0], C[1], p, a, b);
			return result;
	    }
	    
	    
	    /**
	     * Bestimmt zuerst eine Repräsentation der gegebenen Nachricht m als Punkt auf der elliptischen Kurve und berechnet dann die zugehörige Verschlüsselung
	     * @throws Exception 
	     */
	    
	    
	    public BigInteger[] messageEncrypt(BigInteger m) throws Exception
	    {
			BigInteger[] point = {BigInteger.ZERO, BigInteger.ZERO};
			for(int j = 0; j <= 128; j++){
				point[0] = BigInteger.valueOf(128).multiply(m).add(BigInteger.valueOf(j));

				if(point[0].compareTo(p) == 1){
					point[0] = BigInteger.ZERO;
					point[1] = BigInteger.ZERO;
					break;
				}
				BigInteger s = point[0].pow(3).add(a.multiply(point[0])).add(b);
				point[1] = s.myModSqrt(p);
				if(!point.equals(BigInteger.ZERO)){
					break;
				}
			}
			BigInteger result[] = elliptEncrypt(point);
			return result;
	    }
	    
	    
	    /**
	     * Bestimmt den durch das Chiffrat (B,C) verschlüsselten Punkt auf der Kurve und berechnet daraus die (durch eine Zahl repräsentierte) versendete Nachricht.
	     * @throws Exception 
	     */
	    
	    
	    
	    public BigInteger messageDecrypt(BigInteger[] B, BigInteger[] C) throws Exception
	    {
	    	BigInteger result = BigInteger.ZERO;
			BigInteger[] temp = {BigInteger.ZERO, BigInteger.ZERO};
			temp = elliptDecrypt(B, C);
			result = temp[0].divide(BigInteger.valueOf(128));


	    	
	    	return result;
	    	
	    }
	 


	  /************************************************************************
	   ************************************************************************
	   * Methoden, die fertig vorgegeben sind.
	   ************************************************************************
	   ************************************************************************/

	  public ElGamalEllipt() {
	  }

	  public void setPrimeNumber(BigInteger prime) {
	    p = prime;
	  }
	  
	  public void setParam_a(BigInteger param_a)
	  {
		  a = param_a;
	  }
	  
	  public void setParam_b(BigInteger param_b)
	  {
		  b = param_b;
	  }
	  
	  public void setP(BigInteger[] point)
	  {
		  P[0] = point[0];
		  P[1] = point[1];
	  }
	  
	  public void setKeyAlice(BigInteger keyAlice) throws Exception 
	  {
		  kA = keyAlice;
		  A = P[0].elliptMultiply(P[1], kA, p, a, b);
	  }
	  
	  public void setKeyBob(BigInteger keyBob)
	  {
		  kB = keyBob;
	  }
	  
	}
