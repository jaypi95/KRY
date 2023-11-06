package kryptotrainer;

import mybiginteger.*;

import java.util.Random;

/**
 * <p>Title: KryptoTrainer</p>
 * <p>Description: Übungsumgebung für das Wahlfach Kryptologie</p>
 * <p>Copyright: Copyright (c) 2006 / Samuel Beer</p>
 * <p>Company: Zürcher Hochschule Winterthur</p>
 * @author Samuel Beer
 * @version 1.0
 */

public class ElGamal {

  int bitLengthPublicKey;          // Länge der Primzahl p in Bits

  BigInteger[] publicKeyAlice;     // Öffentlicher Schlüssel (p,g,A) von Alice

  BigInteger privateKeyAlice;      // Privater Schlüssel a von Alice

  BigInteger plainText;            // Klartext Bob -> Alice

  BigInteger[] cipheredText;       // Chiffrat (B,c) Bob -> Alice

  BigInteger decipheredText;       // Dechiffrierter Text Bob -> Alice


  /************************************************************************
   ************************************************************************
   * Methoden, die ausprogrammiert werden müssen.
   ************************************************************************
   ************************************************************************/

  /**
   * Öffentlichen Schlüssel (p,g,A) und privaten Schlüssel (a) für Alice
   * generieren und in publicKeyAlice bzw. privateKeyAlice speichern.
   */
  public void generateKeyPair() {
    Random rnd = new Random();
    BigInteger.createTableOfPrimes(100);
    BigInteger p = BigInteger.myProbableSafePrime(this.bitLengthPublicKey, 10, rnd);
    BigInteger g = generateRandomNumber(p);
    BigInteger a = generateRandomNumber(p);
    BigInteger A = g.modPow(a, p);
    publicKeyAlice = new BigInteger[] {p, g, A};
    privateKeyAlice = a;
  }

  /**
   * Chiffrat (B,c) Bob -> Alice erstellen und in cipheredText abspeichern.
   */
  public void createCipheredText() {
    BigInteger m = this.plainText;
    BigInteger p = publicKeyAlice[0];
    BigInteger g = publicKeyAlice[1];
    BigInteger A = publicKeyAlice[2];
    BigInteger b = generateRandomNumber(p);
    BigInteger B = g.modPow(b, p);
    BigInteger c = m.multiply(A.modPow(b, p)).mod(p);
    cipheredText = new BigInteger[] {B, c};
  }

  /**
   * Dechiffrierten Text Bob -> Alice erstellen und in decipheredText abspeichern.
   */
  public void createDecipheredText() {
    BigInteger B = cipheredText[0];
    BigInteger c = cipheredText[1];
    BigInteger p = publicKeyAlice[0];
    BigInteger a = privateKeyAlice;
    BigInteger m = c.multiply(B.modPow(a.negate(), p)).mod(p);
    decipheredText = m;
  }

  private BigInteger generateRandomNumber(BigInteger max){
    Random rnd = new Random();
    BigInteger result = BigInteger.ZERO;
    do {
      result = BigInteger.myProbableSafePrime(max.bitLength(), 10, rnd);
    } while(result.compareTo(max) >= 0 && !result.equals(BigInteger.ONE));
    return result;
  }

  /************************************************************************
   ************************************************************************
   * Methoden, die fertig vorgegeben sind.
   ************************************************************************
   ************************************************************************/

  public ElGamal() {
  }

  public void setBitLength(int len) {
    bitLengthPublicKey = len;
  }

  public void setPlainText(BigInteger plain) {
    plainText = plain;
  }

  public BigInteger[] getCipheredText() {
    return cipheredText;
  }

  public BigInteger getDecipheredText() {
    return decipheredText;
  }

  public BigInteger[] getPublicKey() {
    return publicKeyAlice;
  }

  public BigInteger getPrivateKey() {
    return privateKeyAlice;
  }
}
